
from flask import render_template, Blueprint
from app import data_init


datasets,datasets_name,examples = data_init.load_data()
main = Blueprint('main', __name__)




@main.route('/contact/')
def contact():
    return render_template('contact.html')
@main.route('/about/')
def about():
    return render_template('about.html')
@main.route('/faq/')
def faq():
    return render_template('faq.html')
@main.route('/download/')
def download():
    return render_template('download.html')
@main.route('/sig_yeast/')
def sig_yeast():
    return render_template('sig_yeast.csv')
@main.route('/sig_human_disopred3/')
def sig_human_disopred3():
    return render_template('sig_human_disopred3.csv')
@main.route('/sig_human_SPOTd/')
def sig_human_SPOTd():
    return render_template('sig_human_SPOTd.csv')
@main.route('/sig_yeast_2020/')
def sig_yeast_2020():
    return render_template('sig_yeast_2020.csv')

@main.route('/cluster/')
def cluster():
    return render_template('cluster.html')
@main.route('/yeast_cdt/')
def yeast_cdt():
    return render_template('tz_evolsig_clusterplot_mar13.cdt')
@main.route('/yeast_gtr/')
def yeast_gtr():
    return render_template('tz_evolsig_clusterplot_mar13.gtr')
@main.route('/yeast_jtv/')
def yeast_jtv():
    return render_template('tz_evolsig_clusterplot_mar13.jtv')
@main.route('/elife_supp1/')
def elife_supp1():
    return render_template('Feature_symbol.csv')
@main.route('/table/')
def table():
    return render_template('table.html')








