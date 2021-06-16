def prediction(duration = "12:30" , date = "18-5-2021" , dep_time = "5:45" , Stops = 1 , airline = "Jet Airways" , source = "Kolkata" , destination = "Banglore" , additional = "In-flight meal not included"):


    import pickle
    import pandas as pd
    import numpy as np

    model = pickle.load(open("model.pkl" , "rb"))

    scaler = pickle.load(open("scaler.pkl" , "rb"))


    line = ["Air Asia" , "Air India" , "GoAir" , "IndiGo" , "Jet Airways" , "Jet Airways Bussiness" , "Multiple carriers" , "Multiple carriers Premium economy" , "SpiceJet" , "Trujet" , "Vistara" , "Vistara Premium economy"]
    sour = ["Banglore" , "Chennai" , "Delhi" , "Kolkata" , "Mumbai"]
    dest = ["Delhi" , "New Delhi" , "Kolkata" , "Hyderabad" , "Cochin" , "Banglore"]
    adp = ["1 Long layover" , "1 Short layover" , "2 Long layover" , "Business class" , "Change airports" , "In-flight meal not included" , "No Info" , "No check-in baggage included" , "Red-eye flight"]


    duration = pd.to_datetime(duration).hour * 60 + pd.to_datetime(duration).minute
    day = pd.to_datetime(date).day
    month = pd.to_datetime(date).month
    dep_hour = pd.to_datetime(dep_time).hour
    dep_minute = pd.to_datetime(dep_time).minute


    final_a = {}
    for i in line:
        if airline == i:
            final_a["Airline_{}".format(i)] = 1
        else:
            final_a["Airline_{}".format(i)] = 0

    final_s = {}
    for i in sour:
        if source == i:
            final_s["Source_{}".format(i)] = 1
        else:
            final_s["Source_{}".format(i)] = 0

    final_d = {}
    for i in dest:
        if destination == i:
            final_d["Destination_{}".format(i)] = 1
        else:
            final_d["Destination_{}".format(i)] = 0



    final_ad = {}
    for i in adp:
        if additional == i:
            final_ad["Additional_Info_{}".format(i)] = 1
        else:
            final_ad["Additional_Info_{}".format(i)] = 0

    dur = {"Duration" : duration}
    da = {"day" : day}
    mon = {"month" : month}
    de_h = {"dep_hour" : dep_hour}
    de_m = {"dep_minute" : dep_minute}
    st = {"Stops" : Stops}

    al = {**dur , **da , **mon , **de_h , **de_m , **st , **final_a , **final_s , **final_d , **final_ad}


    final = pd.DataFrame(al , index = [0])
    final.drop(["Destination_Banglore" , "Destination_Kolkata" , "Destination_Hyderabad" , "Destination_Cochin"] , axis = 1 , inplace = True)

    for i in ['Duration','day','month','dep_hour','dep_minute']:
        final[i] = np.log(final[i] + 1)

    final[["Duration" , "day" , "month" , "dep_hour" , "dep_minute"]] = scaler.transform(final[["Duration" , "day" , "month" , "dep_hour" , "dep_minute"]])

    preds = model.predict(final)
    return preds


# x  = prediction("12:30" , "18-5-2021" , "5:45" , 1 , "Jet Airways" , "Kolkata" , "Banglore" , "In-flight meal not included")
# print(x)
