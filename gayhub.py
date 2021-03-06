import httpx as requests
from mirai import *
from HApp import HApp


class Gay(HApp):
    def __init__(self):
        print("Plugin (gayhub) is Loaded")
        self.__username = ''
        self.__gayURL = ''
        self.__result = ''
        self.__msg = ''
        self.whitelist = [
            776324219,
            341475083,
        ]

    def __makeData(self):
        try:
            self.__result = requests.get(url=self.__gayURL, timeout=5).json()
            result = self.__result
            try:
                a = 0
                for i in result:
                    description = str(i['description'])
                    name = str(i['name'])
                    if a > 4:
                        break
                    if description is None:
                        continue

                    if len(description) > 20:
                        description = description[0:21] + '...'

                    if len(name) > 20:
                        name = name[0:21] + '...'

                    self.__msg += "仓库名称: " + str(name) + ' | ' + "STAR: " + str(
                        i['stargazers_count']) + " | 仓库描述: " + str(description) + '\n'
                    a += 1
            except TypeError as ee:
                self.__msg = str('Not Found User!' + self.__username)

        except TimeoutError as e:
            self.__msg = str(e)

    async def recv(self, app: Mirai, event: GroupMessage):
        if HApp.isblocked(self, event.sender.group.id):
            return
        resp = event.messageChain.toString()
        if 'github' in resp:
            self.__msg = ''
            self.__username = resp.replace('github', '').strip()
            self.__gayURL = 'https://api.github.com/users/{}/repos'.format(self.__username)
            self.__makeData()
            await app.sendGroupMessage(event.sender.group,
                                       [Plain(self.__msg + '...')])



if __name__ == '__main__':
    print(Gay('mzdluo123').getMsg())
