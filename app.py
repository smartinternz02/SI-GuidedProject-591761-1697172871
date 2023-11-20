from flask import Flask, render_template, request
import pickle

app=Flask(__name__)
model=pickle.load(open('logi.pkl','rb'))

@app.route('/')
@app.route('/home',methods=['GET', 'POST'])
def Home():
    return render_template("index.html")

@app.route('/predict',methods=['GET', 'POST'])
def Pred():
    return render_template("Predict.html")

@app.route('/result',methods=['GET', 'POST'])
def Result():
    if request.method == "POST":
       satisfaction_level = request.form['satisfaction_level']
       last_evaluation = request.form['last_evaluation']
       number_project	= request.form['number_project']
       average_monthly_hours = request.form['average_monthly_hours']
       time_spend_company = request.form['time_spend_company']
       Work_accident = request.form['Work_accident']
       left = request.form['left']
       promotion_last_5years = request.form['promotion_last_5years']
       salary = request.form['salary']
       
       pred = [[float(satisfaction_level), float(last_evaluation), float(number_project),
                float(average_monthly_hours), float(time_spend_company), float(Work_accident), float(left), 
                float(promotion_last_5years), float(salary)]]
       print(pred)
       output = model.predict(pred)
       print(output)
        
        
       return render_template("results.html",predict="The Predicted Risk value is: "+str(output[0]))

    
if __name__=='__main__':
    app.run(debug=True)