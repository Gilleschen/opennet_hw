from selenium import webdriver
from locator import TwitchLocator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import TimeoutException


class Actions:
    def __init__(self, driver: webdriver):
        self.wait_driver_timeout = 5
        self.driver = driver
        self.twitch_locator = TwitchLocator()
        
     
    def home_page_navigate_to_home_page(self, url: str):
        self.driver.get(url)
        
    def home_page_navigate_to_directory(self, url: str):
        self.driver.get(url + '/directory')
        
    def home_page_sendkey_to_search_bar(self, message: str):
        driver_wait = WebDriverWait(self.driver, self.wait_driver_timeout)
        driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.twitch_locator.search_bar))).click()
        driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.twitch_locator.search_bar))).send_keys(message)
        driver_wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.twitch_locator.search_bar))).send_keys(Keys.ENTER)
        
        
    def switch_search_result_tab_list(self, index: str):
        #index = 0: Top; 1: Channels; 2: Categories; 3: Video
        driver_wait = WebDriverWait(self.driver, self.wait_driver_timeout)
        driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.twitch_locator.tablist_items(index)))).click()
        driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.twitch_locator.channel_list)))
        
    def scroll_page(self, direction="down", times=1):
        top_bar = self.driver.find_element(By.CSS_SELECTOR, self.twitch_locator.top_bar)
        top_bar_height = top_bar.size['height']
        full_size = self.driver.get_window_size()
        start_y = int(full_size['height'] * 0.8)
        end_y = int(top_bar_height)
        scroll_distance = start_y - end_y
        if direction == "down":
            scroll_distance = start_y - end_y
        elif direction == "up":
            scroll_distance = -(start_y - end_y)
        else:
            scroll_distance = start_y - end_y
            
        for i in range(times):
            self.driver.execute_script(f"window.scrollBy({{top: {scroll_distance},behavior: 'smooth'}});")
            time.sleep(2)
    
    
    def click_streamer_live_button(self):
        streamers = self.driver.find_elements(By.CSS_SELECTOR, self.twitch_locator.streamer_list)
        viewport_height = self.driver.execute_script("return window.innerHeight")
    
        try:
            home_button = self.driver.find_element(By.CSS_SELECTOR, self.twitch_locator.navigation_bar_home_button)
            nav_bar = self.driver.execute_script("return arguments[0].parentElement;", home_button)    
            nav_bar_rect = self.driver.execute_script("return arguments[0].getBoundingClientRect();",nav_bar)
            
            bottom_bar_height = viewport_height - nav_bar_rect['top']
        except:
            # if not found, default 56
            bottom_bar_height = 56
        
        effective_viewport_height = viewport_height - bottom_bar_height
        
        # print(f"Effective: {effective_viewport_height}")
        clickable_and_visible_streamers = []
        for index, streamer in enumerate(streamers):
        
            streamer_rect = self.driver.execute_script("return arguments[0].getBoundingClientRect();", streamer)
            # check streamer button can see in the windows
            if streamer_rect['bottom'] > 0 and streamer_rect['top'] < effective_viewport_height:
                clickable_and_visible_streamers.append(streamer)
                streamer_name = streamer.get_attribute('title')
                print(f"Element {index}: Tag={streamer.tag_name}, Name={streamer_name}")
        
        streamer_count = len(clickable_and_visible_streamers)
        print(f'Total streamers：{streamer_count}')
        import random
        # Randomly select a streamer and click
        random_streamer = random.choice(clickable_and_visible_streamers)
        random_streamer.click()
        
        
    def take_a_screenshot(self):
        import datetime
        file_name = 'test_' + (datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'))
        self.driver.get_screenshot_as_file(f"./screenshot/{file_name}.png")
        

    def chekc_stream_live_view_is_ready(self, timeout=10):
        try:  # check the classification note
            WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.twitch_locator.classification_start_watch_button))).click()
        except TimeoutException:
            pass

        try:
            # Wait for video loding
            end_time = time.time() + timeout
            while time.time() < end_time:
              is_playing = self.driver.execute_script("""
                    const video = document.querySelector('video');
                    if (!video) {
                        return false;
                    }
                    return (
                        video.readyState >= 3 &&
                        video.currentTime > 0 &&
                        !video.paused &&
                        video.videoWidth > 0 &&
                        video.videoHeight > 0
                    );
                """)
            if is_playing:
                print('Start Streaming....')
                return True
      
        except TimeoutException:
            print("Timeout...")
            return False
