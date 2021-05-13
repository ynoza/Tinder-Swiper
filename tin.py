from selenium import webdriver
import time

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Yash Oza\tinder_bot\chromedriver.exe")

    def login_with_gmail(self):
        time.sleep(2)
        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email=self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email.send_keys('') #put username here
        next=self.driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next.click()
        time.sleep(2)
        passwrd = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        passwrd.send_keys('') #put pass here
        next=self.driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next.click()
        # you have successfully logged in

        #switch your window back
        self.driver.switch_to_window(base_window)

        while(1):
            try:
                time.sleep(5)
                popup_1=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                popup_1.click()
                break
            except:
                time.sleep(3)
                gg_button=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
                gg_button.click()

    def login_with_fb(self):
        popup_1=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        popup_1.click()

        base_window=self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email=self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys('') #put username here
        passwrd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passwrd.send_keys('') #put pass here
        next=self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        next.click()
        time.sleep(2)
        try:
            continue_as_yash=self.driver.find_element_by_xpath('//*[@id="u_0_4"]/div[2]/div[1]/div[1]/button')
            continue_as_yash.click()
        except:
            pass
        # you have successfully logged in

        #switch your window back
        self.driver.switch_to_window(base_window)

        while(1):
            try:
                time.sleep(3)
                popup_1=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
                popup_1.click()
                break
            except:
                pass


    def login(self):
        self.driver.get('https://tinder.com')
        time.sleep(5)
        try:
            gg_button=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[1]/div/button')
            gg_button.click()
            self.login_with_gmail()
        except:
            self.login_with_fb()
        finally:
            time.sleep(2)
            cookies = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div/button')
            cookies.click()

            popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
            popup_2.click()

            time.sleep(3)

    def like(self):
        like_button=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    def dislike(self):
        dislike_button=self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_button.click()

    def close_popup(self):
        popup_3=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup=self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

    def out_of_likes(self):
        no_likes_popup=self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        no_likes_popup.click()

    def auto_swipe(self):
        while True:
            time.sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except:
                    try:
                        self.close_match()
                    except:
                        self.out_of_likes()
                        break

    def message_matches(self):
        while True:
            try: #need to change the div[3] part in message to div[2] for it to function correctly
                message=self.driver.find_element_by_xpath('//*[@id="matchListNoMessages"]/div[1]/div[3]/a/div[1]')
                message.click()
                message_text=self.driver.find_element_by_xpath('//*[@id="chat-text-area"]')
                message_text.send_keys('Hey')
                send_message=self.driver.find_element_by_xpath ('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/button')
                send_message.click()
                time.sleep(2)
            except:
                break

bot=TinderBot()
bot.login()
bot.auto_swipe()
bot.driver.close()
