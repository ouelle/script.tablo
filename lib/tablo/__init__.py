import _included_packages
import api

API = api.API
Show = api.Show
Channel = api.Channel
Airing = api.Airing
Series = api.Series
Movie = api.Movie
Sport = api.Sport
Program = api.Program
GridAiring = api.GridAiring
APIError = api.APIError


def setUserAgent(agent):
    api.USER_AGENT = agent
