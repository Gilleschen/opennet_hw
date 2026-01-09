class TwitchLocator:
    def __init__(self):
 
        self.search_bar = '[id="twilight-sticky-header-root"] input'
        self.tablist_items = lambda index: f'[role="tablist"] [data-index="{index}"]'
        self.top_bar = '[id="page-main-content-wrapper"] nav'
        self.channel_list = '[role="list"]'
        self.streamer_list = '[id="page-main-content-wrapper"] [role="list"] button h2'
        self.navigation_bar_home_button = 'a[href="/home"]'
        
        ''' Live stream page '''
        self.classification_start_watch_button = '[data-a-target="content-classification-gate-overlay-start-watching-button"]'
        self.live_view_windows = '[data-a-target="video-player"] video'
        
        
        