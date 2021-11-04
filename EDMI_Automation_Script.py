from selenium import webdriver #BusinessAutomation
import time
import keyboard


url_tutorialsninja = "http://www.tutorialsninja.com/demo/"
f_name = "ECHO"
l_name = "ALPHA"
email = "echoalpha12@gmail.com"
telephone = "0322381678"
password = "echo@alpha12345"


#initialize webdriver
tutorialsninja = webdriver.Chrome()
tutorialsninja.maximize_window()
#URL/Website
tutorialsninja.get(url_tutorialsninja)
time.sleep(5)


#Register Account 
if tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a"):
    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a").click() 
    print("My Account......")
    time.sleep(2)
    if tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a"):
        tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a").click()
        print("Welcome to Registration Page.....")
        time.sleep(3)
        #Create Account
        if tutorialsninja.find_element_by_css_selector("#content > h1"):
            tutorialsninja.find_element_by_css_selector("#content > h1").click()
            print("Register Account Header is visible")
            time.sleep(2)
            tutorialsninja.find_element_by_id("input-firstname").send_keys(f_name)
            print("Successfully Input First Name...")
            time.sleep(1)
            tutorialsninja.find_element_by_id("input-lastname").send_keys(l_name)
            print("Successfully Input Last Name...")
            time.sleep(1)
            tutorialsninja.find_element_by_id("input-email").send_keys(email)
            print("Successfully Input Email...")
            time.sleep(1)
            tutorialsninja.find_element_by_id("input-telephone").send_keys(telephone)
            print("Successfully Input Telephone")
            time.sleep(2)
            tutorialsninja.find_element_by_id("input-password").send_keys(password)
            time.sleep(1)
            tutorialsninja.find_element_by_id("input-confirm").send_keys(password)
            print("Successfully Input password")
            time.sleep(3)

            #Subscribe and Confirm Account
            if tutorialsninja.find_element_by_css_selector("#content > form > fieldset:nth-child(3) > div > div > label:nth-child(1) > input[type=radio]"):
                tutorialsninja.find_element_by_css_selector("#content > form > fieldset:nth-child(3) > div > div > label:nth-child(1) > input[type=radio]").click()
                print("Successfully Subscribe...")
                time.sleep(2)
                #Privacy Policy
                tutorialsninja.find_element_by_css_selector("#content > form > div > div > input[type=checkbox]:nth-child(2)").click()
                time.sleep(2)
                tutorialsninja.find_element_by_css_selector("#content > form > div > div > input.btn.btn-primary").click()
                print("Successfully Click the Continue")
                time.sleep(5)
                tutorialsninja.find_element_by_css_selector("#content > div > div > a").click()
                print("ACCOUNT CONFIRMED...")
                time.sleep(3)

                if tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a"):
                    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a").click()
                    print("My Account...")
                    time.sleep(3)
                    #Logout
                    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a").click()
                    time.sleep(5)                               


                else:
                    print("Error 101...")                      
                                    

            

            else:
                print("Error 101...")

        else:
            print("Error 101....")
        

    else:
        print("Error 101...")

else:
    print("Error 101...")


#####################################################################################################


#Login
if tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a"):
    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a").click()
    print("My Account...")
    time.sleep(2)
    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a").click()
    time.sleep(2)
    tutorialsninja.find_element_by_id("input-email").send_keys(email)
    time.sleep(1)
    tutorialsninja.find_element_by_id("input-password").send_keys(password)
    time.sleep(2)
    tutorialsninja.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input").click()
    #tutorialsninja.find_element_by_id("#content > div > div:nth-child(2) > div > form > input").click()
    print("Welcome to Tutorials Ninja App...")
    time.sleep(5)

else:
    print("Error 101")   

######################################################################

#Phone and PDAs
if tutorialsninja.find_element_by_css_selector("#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a"):
    tutorialsninja.find_element_by_css_selector("#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul > li:nth-child(6) > a").click()
    print('Successfully Clicked the Phone and PDAs.........')
    time.sleep(2)
    if tutorialsninja.find_element_by_css_selector("#content > h2"):
        tutorialsninja.find_element_by_css_selector("#content > h2").click()
        print("Phone and PDAs Header were showed.....")
        time.sleep(2)
    
    else:
        print("Phone and PDAs Header were not recognized.... ")

else:
    print("Unsucessfully Click the Phone and PDAs...... Error 101")


#####################################################################################

#Choosing an iPhone

if tutorialsninja.find_element_by_css_selector("#content > div:nth-child(3) > div:nth-child(2) > div > div.image > a > img"):
    tutorialsninja.find_element_by_css_selector("#content > div:nth-child(3) > div:nth-child(2) > div > div.image > a > img").click()
    print("Successfully Clicked the iphone..... ")
    time.sleep(2)
    if tutorialsninja.find_element_by_css_selector("#content > div:nth-child(1) > div.col-sm-4 > div.btn-group > button:nth-child(1)"):
        tutorialsninja.find_element_by_css_selector("#content > div:nth-child(1) > div.col-sm-4 > div.btn-group > button:nth-child(1)").click()
        print("Added to the Wish List...")
        time.sleep(2)
        tutorialsninja.find_element_by_css_selector("#content > div:nth-child(1) > div.col-sm-4 > div.btn-group > button:nth-child(2)").click()
        print("Added to Comparison...")
        time.sleep(2)
        #Click item
        tutorialsninja.find_element_by_css_selector("#content > div:nth-child(1) > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a").click()
        time.sleep(2) 
        #Close Item
        tutorialsninja.find_element_by_css_selector("body > div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready > div > div.mfp-content > div > button").click()
        time.sleep(2)    
        #Quantity of item
        tutorialsninja.find_element_by_css_selector("#input-quantity").click()
        time.sleep(2)
        keyboard.press_and_release('Ctrl + a')
        time.sleep(1)
        keyboard.write("15")
        time.sleep(2)
        tutorialsninja.find_element_by_id("button-cart").click()
        print("Added to Card)")
        time.sleep(3)
        tutorialsninja.find_element_by_css_selector("#cart > button").click()
        time.sleep(2)
        tutorialsninja.find_element_by_css_selector("#cart > ul > li:nth-child(2) > div > p > a:nth-child(1) > strong").click()
        print("Viewing the Cart...")
        time.sleep(2)
        tutorialsninja.find_element_by_css_selector("#content > div.buttons.clearfix > div.pull-right > a").click()
        print("Checked out...")
        time.sleep(2)
    else:
        print("Error 101")
    #LOGOUT
    if tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a"):
                    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown > a").click()
                    print("My Account...")
                    time.sleep(3)
                    #Logout
                    tutorialsninja.find_element_by_css_selector("#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a").click()
                    time.sleep(5)         


    else:
        print("Error 101...")




else:
    print("Unsuccessfully click the iphone.... .Error 101")


#find id
#find name 
#find xpath 
#find css selector
#find class name
