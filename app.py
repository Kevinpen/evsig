
from flask import Flask, render_template, request
import sig



app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
      if 'submit' in request.form:
          datasets = request.form.get('dataset') # Get dataset info
          if datasets=="Yeast_elife_2019":
              dataset=0
          elif datasets=="Human": 
              dataset=1
          elif datasets=="Yeast_2020": 
              dataset=2    
          cid= request.form.get('cid') # User input protein common name
          sid= request.form.get('sid')# User input protein systematic name
          idrname = str(request.form.get('idrname'))# User input IDR name
          if cid:
              name = sig.getindex_cid(cid, dataset)
              if name==[]:
                  return render_template("message.html", message="Sorry, can't find any protein by that name in this dataset, please check the name or dataset.")
              elif len(name)>1:
                  return render_template("choice.html", name=name, cid=cid, dataset=dataset)
              else:
                  index=sig.getindex_idr(name[0], dataset)
    
          
          elif sid:
              name = sig.getindex_sid(sid, dataset)
              if name==[]:
                  return render_template("message.html", message="Sorry, can't find any protein by that name in this dataset, please check the name or dataset.")
              elif len(name)>1:
                  return render_template("choice.html", name=name, cid=sid, dataset=dataset)
              else:
                  index=sig.getindex_idr(name[0], dataset)

          
          elif idrname:
              index = sig.getindex_idr(idrname, dataset)
              if index == -1:
                      return render_template("message.html", message="Sorry, can't find any IDR by that name in this dataset, please check the name or dataset.", \
                      message2="The format of IDR name is: <protein systematic name>_aa_<start>-<end>" )
          else: 
              return render_template("message.html", message="No input received, Please input either protein name or IDR name before click 'Go!'")
          sig.sigviz(index,"bar", 1,dataset=dataset)
          group = 1
          sig.sigviz(index,"div",group, dataset)
          sig.sigpro(index, dataset)

          #Find list of similar idr
          similist=sig.getsimi(index, dataset)
          name=similist[0] # The first item of list is original IDR
          simi=similist[1:11]
          #Find common name for similar IDRs
          for i in range(10):
              simi_index=sig.getindex_idr(simi[i], dataset)
              simi[i]=simi[i]+";"+(sig.getname(simi_index, dataset))

          group_str=str(group)
          group_list=sig.getgroup(dataset)
          datasetname=sig.get_dataset_name(dataset)
          idrname=""
          cid=""
          sid=""
          return render_template("search.html",dataset=dataset,datasetname = datasetname, gid=str(index),simi=simi, name=name,group=group_str,
                                 group_list=group_list,default1="defaultOpen",default2="other")


    elif request.method == 'GET':
      return render_template("index.html")


@app.route('/contact/')
def contact():
    return render_template('contact.html')
@app.route('/about/')
def about():
    return render_template('about.html')
@app.route('/faq/')
def faq():
    return render_template('faq.html')
@app.route('/download/')
def download():
    return render_template('download.html')
@app.route('/sig_yeast/')
def sig_yeast():
    return render_template('sig_yeast.csv')
@app.route('/sig_human/')
def sig_human():
    return render_template('sig_human.csv')
@app.route('/cluster/')
def cluster():
    return render_template('cluster.html')
@app.route('/yeast_cdt/')
def yeast_cdt():
    return render_template('tz_evolsig_clusterplot_mar13.cdt')
@app.route('/yeast_gtr/')
def yeast_gtr():
    return render_template('tz_evolsig_clusterplot_mar13.gtr')
@app.route('/yeast_jtv/')
def yeast_jtv():
    return render_template('tz_evolsig_clusterplot_mar13.jtv')
@app.route('/elife_supp1/')
def elife_supp1():
    return render_template('Feature_symbol.csv')



@app.route('/search',methods=['POST','GET']) #Response for yeast search
def search():
    #Specify to default open "overview" tab
    default1="defaultOpen"
    default2="other"
    if request.method == 'POST':

      if 'submit_button' in request.form: # Response for user choose other group in diversion plot
          group_tuple = request.form.get('group') #Value get from page submit is tuple of name and group
          if group_tuple is None:
              return render_template("message.html", message="No feature chosen, Please choose one of the molecular features before click 'Go!'")
          idrname=group_tuple.split(",")[0]
          dataset = int(group_tuple.split(",")[2])
          index = sig.getindex_idr(idrname, dataset)
          group=int(group_tuple.split(",")[1])
          sig.sigviz(index,"bar", dataset=dataset)
          sig.sigviz(index,"div",group, dataset)
          sig.sigpro(index, dataset)
          

          #Specify to default open "Detail" tab
          default2="defaultOpen"
          default1="other"
          group_str=group_tuple.split(",")[1]


      elif 'submit_choice_cid' in request.form: #Response for user choose one IDR from multiple IDRs in one protein
          ccid_tuple = str(request.form.get('ccid'))
          #return "{}".format(ccid_tuple)
          if ccid_tuple == "None":
              return render_template("message.html", message="No IDR chosen, Please choose one of the IDRs before click 'Go!'")
          ccid = ccid_tuple.split(",")[0]
          dataset = int(ccid_tuple.split(",")[1])
          index = sig.getindex_idr(ccid, dataset)      
          sig.sigviz(index,"bar", 1, dataset=dataset)
          group = 1
          sig.sigviz(index,"div",group, dataset)
          sig.sigpro(index, dataset)

      elif 'submit_simi' in request.form: #Response for user search similar IDR
          idrname_tuple = str(request.form.get('simi'))
          if idrname_tuple == "None":
              return render_template("message.html", message="No IDR chosen, Please choose one of the IDRs before click 'Go!'")          
          idrname = idrname_tuple.split(",")[0]
          dataset = int(idrname_tuple.split(",")[1])
          index = sig.getindex_idr(idrname, dataset)
          sig.sigviz(index,"bar", dataset=dataset)
          group = 1
          sig.sigviz(index,"div",group, dataset)
          sig.sigpro(index, dataset)

      #Find list of similar idr
      similist=sig.getsimi(index, dataset)
      name=similist[0] # The first item of list is original IDR
      simi=similist[1:11]
      #Find common name for similar IDRs
      for i in range(10):
          simi_index=sig.getindex_idr(simi[i], dataset)
          simi[i]=simi[i]+";"+(sig.getname(simi_index, dataset))
      group_str=str(group)
      idrname=""
      group_list=sig.getgroup(dataset)
      datasetname=sig.get_dataset_name(dataset)
      return render_template("search.html",dataset=dataset, datasetname=datasetname,gid=str(index),simi=simi, name=name,group=group_str,
                             group_list=group_list,default1=default1,default2=default2)

    elif request.method == 'GET':
       return render_template('search.html', gid=str(index), simi=simi,name=name,group=group,default1=default1,default2=default2)





if __name__ == "__main__":
    app.run(debug=True)
