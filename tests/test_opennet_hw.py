import pytest
import logging
from libs.actions import Actions
from locator import TwitchLocator


class TestTwitchWeb:
    twitch_locator = TwitchLocator()

    @pytest.fixture(autouse=True)
    def _setup(self, test_config):
        self.twitchurl = test_config['PROD']['TwitchURL']
        self.gamename = test_config['PROD']['GameName']
        

    def test_01_010_010(self, web_driver_01):
        try:
            device = Actions(web_driver_01)
            
            # Navigate to twitch URL
            # device.home_page_navigate_to_home_page(self.twitchurl)
            
            # Navigate to directory page
            device.home_page_navigate_to_directory(self.twitchurl)
            
            # Send message into search bar and Enter
            device.home_page_sendkey_to_search_bar(self.gamename)
          
            # # Click channel tab
            device.switch_search_result_tab_list(1)
            
            ## Scroll down two times
            device.scroll_page(direction="down", times=2)
        
            ## Click a streamer
            device.click_streamer_live_button()
            
            ## Check live view is ready
            if device.chekc_stream_live_view_is_ready():
            
                # Take s screenshot and save to ./screenshot fold
                device.take_a_screenshot()
                assert True
            else:
                assert False
            
        except Exception as e:
            logging.info(e)
            assert False

