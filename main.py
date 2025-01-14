import smartsheet
import config

if __name__ == "__main__":
    def runScript():
        client = smartsheet.Smartsheet(access_token=config.token)
        me = client.Users.get_current_user()
        return me
runScript()