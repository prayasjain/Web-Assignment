__author__ = 'PRAYAS2'

from flask import Flask ,render_template,request,url_for,make_response
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app=Flask(__name__)



@app.route('/ritvik')
def ritvik():
    return render_template('ritvik.html')

@app.route('/')
def mainpage():
    return render_template('mainpage.html')

@app.route('/average',methods=['GET','POST'])
def average():
    x=''
    if request.method=='GET':
        return render_template('average.html',source=str(x))
    elif request.method=='POST':
        x=str(request.form['points'])
        try:

            l=str(x).split(',')
            l=list(map(int,l))

            return render_template('average.html',source=x+' is '+str(sum(l)/len(l)))
        except :
            return render_template('average.html',source='Invalid Input')
    else :
        return 'Invalid Request'












@app.route('/aboutme')
def prayas():
    return render_template('abme.html')






@app.route('/anubhav')
def anubhav ():
    return render_template('anubhav.html')




@app.route('/graph',methods=['GET','POST'])
def graph():
    plt.clf()
    x=''
    if request.method=='GET':
        return render_template('graph.html')
    elif request.method=='POST':
        pts=str(request.form['points'])
        order=str(request.form['order'])
        area=str(request.form['area'])
        l=pts.split(',')
        order=int(order)
        lp=area.split(',')
        lp=list(map(int,lp))

        l=list(map(int,l))

        try:



            class Integrate : #class to calculate integral of a function from a to b
                def plot(self,order,li,a,b):
                    def f(x) : #function to calculate value of a function for a given x
                        s=0
                        z=0
                        for t in li :
                            s=s+pow(x,z)*t
                            z=z+1
                        return s ;
                    plt.axis([a-3,b+3,-25,25])
                    plt.title('INTEGRATION')
                    plt.xlabel('x axis')
                    plt.ylabel('y axis')
                    plt.plot([float(x) for x in np.arange(a-3,b+3,0.1)],[f(float(x)) for x in np.arange(a-3,b+3,0.1)],'r-',linewidth=1.5)
                    plt.plot([0,0],[-400,400],'k-',[-400,400],[0,0],'k-',linewidth=2.5)
                    plt.grid(True)

                    #plt.show()



                def TrapezoidalRule(self,order,li,a,b) :
                    self.plot(order,li,a,b)
                    def f(x) : #function to calculate value of a function for a given x
                        s=0
                        z=0
                        for t in li :
                            s=s+pow(x,z)*t
                            z=z+1
                        return s ;

                    n= int(b-a)*1000
                    h=(b-a)/n
                    s=f(a)+f(b)
                    for i in range(n-1) :
                        s=s+2*f(a+h*(i+1))     #All values are added twice except the initial and final point which are added just once
                        plt.plot([a+h*(i+1),a+h*(i+1)],[0,f(a+h*(i+1))],color='green')
                    s=s/(2*n)
                    s=s*(b-a)

                    plt.axis([a-3,b+3,-25,25])
                    plt.savefig('static/images/t'+pts+',,'+str(order)+',,,'+area+'.png')
                    return s




            itr=Integrate()
            itr.TrapezoidalRule(order,l,lp[0],lp[1])


            return render_template('plot.html',source='static/images/t'+pts+',,'+str(order)+',,,'+area+'.png')



        except :
            return render_template('graph.html')
    else :
        return 'Invalid Request'


if __name__== '__main__' :

    app.run()