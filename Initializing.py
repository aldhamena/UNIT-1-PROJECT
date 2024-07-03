class Player:

    def __init__(self):   #, name, age, gender, height, weight, ParentPhone, EMail):

        self.info = {"fname":input("Please insert your first name: "),
        "lname": input("Please insert your last name: "),
        "age": int(input("Please insert your age: ")),
        "gender": input("Please insert your gender: 'Male' or 'Female': "),
        "height": int(input("Please insert your height in CM: ")),
        "fheight": int(input("Please insert your father height in CM: ")),
        "mheight": int(input("Please insert your mother height in CM: ")),
        "weight": int(input("Please insert your weight in KG: ")),
        "ParentPhone": int(input("Please insert your parent phone number: ")),
        "EMail": input("Please insert your parent email ending with @Example.exa: "),
        "BMI": 0
        }

        #"BMI": int(("weight" / "height"**2)*10000)

    def Expected_Adult_Age_Height(self):

        try:

            if self.info["gender"].upper() == "MALE": #and all(type(var) is str for var in [self.info["fname", "lname", "gender", "EMail"]])
                self.ExpectedH = (self.info["fheight"] + self.info["mheight"] + 13)/2
                return f"Your Expected height at adult age is {self.ExpectedH}"
            
            elif self.info["gender"].upper() == "FEMALE":
                self.ExpectedH = (self.info["fheight"] + self.info["mheight"] - 13)/2
                return f"Your Expected height at adult age is {self.ExpectedH}"
        
        except:

            print("That was an invalid input")


        #self.BMI = (self.info["weight"] / self.info["height"]**2)*10000

    def Player_BMI(self):

        self.info["BMI"] = round((self.info["weight"] / self.info["height"]**2)*10000,2)        
        return f"Your Body Mass Index is {self.info["BMI"]}"
    
    def suggested_sports(self):

        self.info["BMI"] = round((self.info["weight"] / self.info["height"]**2)*10000,2)
        
        if self.info["BMI"] >= 18.5 and self.info["BMI"] <= 24.9 and self.info["gender"].upper() == "MALE":

            self.ExpectedH = (self.info["fheight"] + self.info["mheight"] + 13)/2

            if self.ExpectedH >= 170.0:
                return "WOW. You're expected to be a tall boy and here is a list of sports that suit you: \n 1- Handball \n 2- Basketball \n 3- Volleyball"
                
            elif self.ExpectedH < 170.0:
                return "You're not expected to be a very tall boy but we have a good list of sports that suit you: \n 1- Football \n 2- Badminton \n 3- Swimming"
            
        elif self.info["BMI"] >= 18.5 and self.info["BMI"] <= 24.9 and self.info["gender"].upper() == "FEMALE":

            self.ExpectedH = (self.info["fheight"] + self.info["mheight"] - 13)/2
            
            if self.ExpectedH >= 160.0:
                return "WOW. You're expected to be a tall girl and here is a list of sports that suit you: \n 1- Handball \n 2- Basketball \n 3- Volleyball"
            
            elif self.ExpectedH < 160.0:
                return "You're not expected to be a very tall girl but we have a good list of sports that suit you: \n 1- Football \n 2- Badminton \n 3- Swimming"
            
            
        elif self.info["BMI"] < 18.5:

            return "You're too skinny. Eat healthy and gain some weight"
        
        else:

            return "You're over weight and need to lose some weight"
                
    def chosen_sport(self):

        if self.info["gender"].upper() == "MALE": # and self.ExpectedH() >= 170: or (self.info["gender"] == "Female" and self.ExpectedH() >= 160):

            self.ExpectedH = (self.info["fheight"] + self.info["mheight"] + 13)/2

            if self.ExpectedH >= 170.0:

                self.choosing = int(input("write the number of the sport you would like to be registered to: "))

                if self.choosing == 1:
                    return "You've chosen handball"
                
                elif self.choosing == 2:
                    return "You've chosen Basketball"
                
                elif self.choosing == 3:
                    return "You've chosen Basketball"
                
            elif self.ExpectedH < 170:

                self.choosing = int(input("write the number of the sport you would like to be registered to: "))

                if self.choosing == 1:
                    return "You've chosen Football"
                
                elif self.choosing == 2:
                    return "You've chosen Badminton"
                
                elif self.choosing == 3:
                    return "You've chosen Swimming"
            
        elif self.info["gender"].upper() == "FEMALE": # and self.ExpectedH() >= 170: or (self.info["gender"] == "Female" and self.ExpectedH() >= 160):

            self.ExpectedH = (self.info["fheight"] + self.info["mheight"] - 13)/2

            if self.ExpectedH >= 160.0:

                self.choosing = int(input("write the number of the sport you would like to be registered to: "))

                if self.choosing == 1:
                    return "You've chosen handball"
                
                elif self.choosing == 2:
                    return "You've chosen Basketball"
                
                elif self.choosing == 3:
                    return "You've chosen Basketball"
                
            elif self.ExpectedH < 160:

                self.choosing = int(input("write the number of the sport you would like to be registered to: "))

                if self.choosing == 1:
                    return "You've chosen Football"
                
                elif self.choosing == 2:
                    return "You've chosen Badminton"
                
                elif self.choosing == 3:
                    return "You've chosen Swimming"
            