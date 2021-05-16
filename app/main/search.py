from flask import render_template, request, Blueprint
from app import data_init
from . import sig, zfplot

datasets,datasets_name,examples = data_init.load_data()
result = Blueprint('result', __name__)


@result.route('/search',methods=['POST','GET']) #Response for yeast search
def search():
    #Specify to default open "overview" tab
    default1="defaultOpen"
    default2="other"
    default3="another"
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
            if dataset == 0:
              annotated = []
              tstats_col = 6
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

            #Specify to default open "Detail" tab
            default2="defaultOpen"
            default1="other"
            group_str=group_tuple.split(",")[1]


        elif 'submit_choice_cid' in request.form: #Response for user choose one IDR from multiple IDRs in one protein
            ccid_tuple = str(request.form.get('ccid'))
            if ccid_tuple == "None":
                return render_template("message.html", message="No IDR chosen, Please choose one of the IDRs before click 'Go!'")
            ccid = ccid_tuple.split(",")[0]
            dataset = int(ccid_tuple.split(",")[1])
            index = sig.getindex_idr(ccid, dataset)      
            sig.sigviz(index,"bar", 1, dataset=dataset)
            group = 1
            sig.sigviz(index,"div",group, dataset)
            sig.sigpro(index, dataset)

            if dataset == 0:
              annotated = []
              tstats_col = 6
            else:
                zfset = dataset-1
                annotated = zfplot.get_ann(index, zfset)
                non_anns = zfplot.get_non_ann(index, zfset)
                if annotated:
                    ann_col = zfplot.get_columnIndex(annotated[0], zfset)
                    tstats_col = zfplot.get_tstats_col(ann_col,zfset)
                    zfplot.plot_scatter(tstats_col,index, zfset)
                else: 
                    ann_col = zfplot.get_columnIndex(non_anns[0], zfset)
                    tstats_col = zfplot.get_tstats_col(ann_col, zfset)
                    zfplot.plot_scatter(tstats_col,index, zfset)
        
        elif 'submit_ann' in request.form:
            ann_tuple =str(request.form.get('anns'))
            if ann_tuple == "None":
                return render_template("message.html", message="No GO terms chosen, Please choose one of the GO terms before click 'Go!'")
            index = int(ann_tuple.split(",")[0])
            dataset = int(ann_tuple.split(",")[3])
            zfset = dataset-1
            ann_col = zfplot.get_columnIndex(ann_tuple.split(",")[1]+','+ann_tuple.split(",")[2], zfset)
            tstats_col = zfplot.get_tstats_col(ann_col, zfset)
            zfplot.plot_scatter(tstats_col,index, zfset)
            sig.sigviz(index,"bar", 1, dataset=dataset)
            group = 1
            sig.sigviz(index,"div",group, dataset)
            sig.sigpro(index, dataset)

            default3="defaultOpen"
            default1="other"

        elif 'submit_non_ann' in request.form:
            non_ann_tuple =str(request.form.get('non_ann'))
            if non_ann_tuple == "None":
                return render_template("message.html", message="No GO terms chosen, Please choose one of the GO terms before click 'Go!'")
            index = int(non_ann_tuple.split(",")[0])
            dataset = int(non_ann_tuple.split(",")[3])
            zfset = dataset-1
            ann_col = zfplot.get_columnIndex(non_ann_tuple.split(",")[1]+','+non_ann_tuple.split(",")[2], zfset)
            tstats_col = zfplot.get_tstats_col(ann_col, zfset)
            zfplot.plot_scatter(tstats_col,index, zfset)
            sig.sigviz(index,"bar", 1, dataset=dataset)
            group = 1
            sig.sigviz(index,"div",group, dataset)
            sig.sigpro(index, dataset)

            
            #Specify to default open "ZFplot" tab
            default3="defaultOpen"
            default1="other"    

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
            if dataset == 0:
              annotated = []
              tstats_col = 6
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

        zfset = dataset-1
        annotated = zfplot.get_ann(index, zfset)
        non_anns = zfplot.get_non_ann(index, zfset)
        group_str=str(group)
        idrname=""
        group_list=sig.getgroup(dataset)
        datasetname=sig.get_dataset_name(dataset)
        sysid=sig.getsys(index,dataset)
        if datasetname.split("_")[0]=="Yeast":
                sysid=sig.getuni(sysid)
        return render_template("search.html",dataset=dataset, datasetname=datasetname,gid=str(index),simi=simi, name=name,sys=sysid,group=group_str, anns=annotated,tstats_col=str(tstats_col),non_anns=non_anns,group_list=group_list,default1=default1,default2=default2,default3=default3)

    elif request.method == 'GET':
       return render_template('search.html', gid=str(index), simi=simi,name=name,group=group, anns=zfplot.tstats[dataset-1].columns, default1=default1,default2=default2,default3=default3)