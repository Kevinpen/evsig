
from flask import Flask, render_template, request
import sig,sigh



app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
      if 'submit' in request.form:
        species = request.form.get('species') # Get species info
        if species == 'Human':
          #User search human idr
          cid= request.form.get('cid') # User input protein common name
          if cid:
              name = sigh.getindex_cid(cid)
              if name==[]:
                  return render_template("message.html", message="Sorry, can't find any protein by that name.")
              elif len(name)>1:
                  return render_template("choiceh.html", name=name, cid=cid)
              else:
                  index=sigh.getindex_idr(name[0])

          sid= request.form.get('sid')# User input protein systematic name
          if sid:
              name = sigh.getindex_sid(sid)
              if name==[]:
                  return render_template("message.html", message="Sorry, can't find any protein by that name.")
              elif len(name)>1:
                  return render_template("choiceh.html", name=name, cid=sid)
              else:
                  index=sigh.getindex_idr(name[0])

          idrname = str(request.form.get('idrname'))# User input IDR name
          if idrname:
              index = sigh.getindex_idr(idrname)
              if index == -1:
                      return render_template("message.html", message="Sorry, can't find any IDR by that name.", \
                      message2="The format of IDR name is: <protein systematic name>_aa_<start>-<end>" )
          sigh.sighviz(index,"bar")
          group = 2
          sigh.sighviz(index,"div",group)
          sigh.sighpro(index)

          #Find list of similar idr
          similist=sigh.simi(index)
          name=similist[0] # The first item of list is original IDR
          simi=similist[1:11]
          #Find common name for similar IDRs
          simicom=[None]*10
          for i in range(10):
              simi_index=sigh.getindex_idr(simi[i])
              simicom[i]=sigh.getname(simi_index)

          group_str=str(group)
          idrname=""
          cid=""
          sid=""
          return render_template("hsearch.html",simi=simi, simicom=simicom,name=name,
                 gid=str(index),group=group_str)

        else:# If user search yeast

          cid= request.form.get('cid') # User input protein common name
          if cid:
              name = sig.getindex_cid(cid)
              if name==[]:
                  return render_template("message.html", message="Sorry, can't find any protein by that name.")
              elif len(name)>1:
                  return render_template("choice.html", name=name, cid=cid)
              else:
                  index=sig.getindex_idr(name[0])

          sid= request.form.get('sid')# User input protein systematic name
          if sid:
              name = sig.getindex_sid(sid)
              if name==[]:
                  return render_template("message.html", message="Sorry, can't find any protein by that name.")
              elif len(name)>1:
                  return render_template("choice.html", name=name, cid=sid)
              else:
                  index=sig.getindex_idr(name[0])

          idrname = str(request.form.get('idrname'))# User input IDR name
          if idrname:
              index = sig.getindex_idr(idrname)
              if index == -1:
                      return render_template("message.html", message="Sorry, can't find any IDR by that name.", \
                      message2="The format of IDR name is: <protein systematic name>_aa_<start>-<end>" )
          sig.sigviz(index,"bar")
          group = 1
          sig.sigviz(index,"div",group)
          sig.sigpro(index)

          #Find list of similar idr
          similist=sig.simi(index)
          name=similist[0] # The first item of list is original IDR
          simi=similist[1:11]
          #Find common name for similar IDRs
          simicom=[None]*10
          for i in range(10):
            simi_index=sig.getindex_idr(simi[i])
            simicom[i]=sig.getname(simi_index)
          group_str=str(group)
          idrname=""
          cid=""
          sid=""
          return render_template("search.html", gid=str(index),simi=simi, simicom=simicom,name=name,group=group_str,default1="defaultOpen",default2="other")

    elif request.method == 'GET':
      return render_template("index.html")




@app.route('/contact/')
def contact():
    return render_template('contact.html')
@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/search',methods=['POST','GET']) #Response for yeast search
def search():
    #Specify to default open "overview" tab
    default1="defaultOpen"
    default2="other"
    if request.method == 'POST':

      if 'submit_button' in request.form: # Response for user choose other group in diversion plot
          group_tuple = request.form.get('group') #Value get from page submit is tuple of name and group
          idrname=group_tuple.split(",")[0]
          index = sig.getindex_idr(idrname)
          group=int(group_tuple.split(",")[1])
          sig.sigviz(index,"bar")
          sig.sigviz(index,"div",group)
          sig.sigpro(index)

          #Specify to default open "Detail" tab
          default2="defaultOpen"
          default1="other"
          group_str=group_tuple.split(",")[1]


      elif 'submit_choice_cid' in request.form: #Response for user choose one IDR from multiple IDRs in one protein
          ccid = str(request.form.get('ccid'))
          index = sig.getindex_idr(ccid)
          sig.sigviz(index,"bar")
          group = 1
          sig.sigviz(index,"div",group)
          sig.sigpro(index)

      elif 'submit_simi' in request.form: #Response for user search similar IDR
          idrname = str(request.form.get('simi'))
          index = sig.getindex_idr(idrname)
          sig.sigviz(index,"bar")
          group = 1
          sig.sigviz(index,"div",group)
          sig.sigpro(index)

      #Find list of similar idr
      similist=sig.simi(index)
      name=similist[0] # The first item of list is original IDR
      simi=similist[1:11]
      #Find common name for similar IDRs
      simicom=[None]*10
      for i in range(10):
          simi_index=sig.getindex_idr(simi[i])
          simicom[i]=sig.getname(simi_index)
      group_str=str(group)
      idrname=""
      return render_template("search.html", gid=str(index),simi=simi, simicom=simicom,name=name,group=group_str,default1=default1,default2=default2)

    elif request.method == 'GET':
       return render_template('search.html',gid=gid,simi=simi,simicom=simicom,name=name,group=group,default1=default1,default2=default2)


@app.route('/hsearch',methods=['POST','GET'])  # Response for human search
def hsearch():
    if request.method == 'POST':
      if 'submit_button' in request.form: # Response for user choose other group in diversion plot
          group_tuple = request.form.get('group') #Value get from page submit is tuple of name and group
          idrname=group_tuple.split(",")[0]
          index = sigh.getindex_idr(idrname)
          group=int(group_tuple.split(",")[1])
          sigh.sighviz(index,"bar")
          sigh.sighviz(index,"div",group)
          sigh.sighpro(index)

      elif 'submit_choice_cid' in request.form: #Response for user choose one IDR from multiple IDRs in one protein
          ccid = str(request.form.get('ccid'))
          index = sigh.getindex_idr(ccid)
          sigh.sighviz(index,"bar")
          group = 2
          sigh.sighviz(index,"div",group)
          sigh.sighpro(index)

      elif 'submit_simi' in request.form: #Response for user search similar IDR
          idrname = str(request.form.get('simi'))
          index = sigh.getindex_idr(idrname)
          sigh.sighviz(index,"bar")
          group = 2
          sigh.sighviz(index,"div",group)
          sigh.sighpro(index)

      #Find list of similar idr
      similist=sigh.simi(index)
      name=similist[0] # The first item of list is original IDR
      simi=similist[1:11]
      #Find common name for similar IDRs
      simicom=[None]*10
      for i in range(10):
            simi_index=sigh.getindex_idr(simi[i])
            simicom[i]=sigh.getname(simi_index)
      group_str=str(group)
      idrname=""

      return render_template("hsearch.html", gid=str(index),simi=simi,simicom=simicom,name=name,group=group_str)
    elif request.method == 'GET':
       return render_template('hsearch.html',gid=gid,simi=simi,simicom=simicom,name=name,group=group)





if __name__ == "__main__":
    app.run(debug=True)
