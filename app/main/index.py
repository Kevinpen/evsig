from flask import render_template, request, Blueprint
from app import data_init
from . import sig, zfplot

datasets,datasets_name,examples = data_init.load_data()
choose = Blueprint('choose', __name__)


@choose.route('/', methods=['POST','GET'])
def index():
    print("h")
           
    if request.method == 'POST':
      if 'submit' in request.form:
          dataset = request.form.get('dataset') # Get dataset info
          if (dataset is None):
                  return render_template("message.html", message="Dataset not selected, Please select dataset and input either protein name or IDR name before click 'Go!'")
          dataset = datasets.index[datasets.iloc[:,0] == dataset][0]
    
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
          if dataset == 0:
              annotated = []
              tstats_col = 6
              non_anns=[]
          else:
            zfset = dataset-1
            annotated = zfplot.get_ann(index, zfset)
            non_anns = zfplot.get_non_ann(index, zfset)
            if annotated:
                ann_col = zfplot.get_columnIndex(annotated[0], zfset)
                tstats_col = zfplot.get_tstats_col(ann_col, zfset)
                zfplot.plot_scatter(tstats_col,index, zfset)
            else: 
                ann_col = zfplot.get_columnIndex(non_anns[0], zfset)
                tstats_col = zfplot.get_tstats_col(ann_col, zfset)
                zfplot.plot_scatter(tstats_col,index, zfset)

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
          sysid=sig.getsys(index,dataset)
          if datasetname.split("_")[0]=="Yeast":
              sysid=sig.getuni(sysid)
          idrname=""
          cid=""
          sid=""
          return render_template("search.html",dataset=dataset,datasetname = datasetname, gid=str(index),simi=simi, name=name,sys=sysid,group=group_str, anns=annotated,tstats_col=str(tstats_col), non_anns=non_anns, group_list=group_list, default1="defaultOpen", default2="other", default3='another')


    elif request.method == 'GET':
      return render_template("index.html",datasets_name=datasets_name,examples=examples)