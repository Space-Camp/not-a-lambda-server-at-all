from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('take', api.take),
    url('drop', api.drop),
    url('status', api.status),
    url('sell', api.sell),
    url('wear', api.wear),
    url('undress', api.remove),
    url('examine', api.examine),
    url('change_name', api.change_name),
    url('pray', api.pray),
    url('fly', api.fly),
    url('dash', api.dash),
    url('player_state', api.player_state),
    url('transmogrify', api.gamble),
    url('carry', api.carry),
    url('receive', api.receive),
    url('warp', api.warp),
    url('recall', api.recall),
    url('create', api.create_world)

]
