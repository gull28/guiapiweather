import tkinter as tk
import json
import requests


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=riga&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"

        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both", expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"])+" hPa").pack(side="top", fill="both", expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top", fill="both", expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=moscow&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both", expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"])+ " hPa").pack(side="top", fill="both", expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top", fill="both", expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both", expand=True)



class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=london&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"]) + " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=berlin&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"])+ " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=new%20york&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"])+ " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=toronto&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"])+ " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class Page7(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=beijing&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"])+ " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class Page8(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=mumbai&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"]) + " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class Page9(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=cairo&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"]) + " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class Page10(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        try:
            api_req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=santiago&appid=&units=metric")
            apijson = json.loads(api_req.content)
        except tk.EXCEPTION as error:
            apijson = "Error"
        apilbl_cntry = tk.Label(self, text="Country: " + str(apijson["sys"]["country"])).pack(side="top", fill="both",expand=True)
        apilbl_city = tk.Label(self, text="City: " + str(apijson["name"])).pack(side="top", fill="both", expand=True)
        api_temp = tk.Label(self, text="Current temperature: " + str(apijson["main"]["temp"]) + "°C").pack(side="top",fill="both",expand=True)
        api_temp_min = tk.Label(self, text="Min temperature: " + str(apijson["main"]["temp_min"]) + "°C").pack(side="top", fill="both", expand=True)
        api_temp_max = tk.Label(self, text="Max temperature: " + str(apijson["main"]["temp_max"]) + "°C").pack(side="top", fill="both", expand=True)
        api_pressure = tk.Label(self, text="Pressure: " + str(apijson["main"]["pressure"])+ " hPa").pack(side="top",fill="both",expand=True)
        api_humidity = tk.Label(self, text="Humidity: " + str(apijson["main"]["humidity"])).pack(side="top",fill="both",expand=True)
        api_sky = tk.Label(self, text="Sky: " + (apijson["weather"][0]["description"])).pack(side="top", fill="both",expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)
        p7 = Page7(self)
        p8 = Page8(self)
        p9 = Page9(self)
        p10 = Page10(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p9.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p10.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Riga", command=p1.show)
        b2 = tk.Button(buttonframe, text="Moscow", command=p2.show)
        b3 = tk.Button(buttonframe, text="London", command=p3.show)
        b4 = tk.Button(buttonframe, text="Berlin", command=p4.show)
        b5 = tk.Button(buttonframe, text="New York", command=p5.show)
        b6 = tk.Button(buttonframe, text="Toronto", command=p6.show)
        b7 = tk.Button(buttonframe, text="Beijing", command=p7.show)
        b8 = tk.Button(buttonframe, text="Mumbai", command=p8.show)
        b9 = tk.Button(buttonframe, text="Cairo", command=p9.show)
        b10 = tk.Button(buttonframe, text="Santiago", command=p10.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        b7.pack(side="left")
        b8.pack(side="left")
        b9.pack(side="left")
        b10.pack(side="left")


        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("WeatherView")
    root.iconbitmap("images/sunny.ico")
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("500x300")
    root.mainloop()
