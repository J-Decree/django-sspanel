from django.urls import path
from . import views

app_name = "api"
urlpatterns = [
    path("system_status/", views.SystemStatusView.as_view(), name="system_status"),
    path("user/settings/", views.UserSettingsView.as_view(), name="user_settings"),
    path("subscribe/", views.SubscribeView.as_view(), name="subscribe"),
    path("reset_ss_port/", views.ReSetSSPortView.as_view(), name="reset_ss_port"),
    path("gen/invitecode/", views.gen_invite_code, name="geninvitecode"),
    path("shop/", views.purchase, name="purchase"),
    path("change/theme/", views.change_theme, name="change_theme"),
    path("change/sub_type/", views.change_sub_type, name="change_sub_type"),
    path("checkin/", views.UserCheckInView.as_view(), name="checkin"),
    # web api 接口
    path("nodes/<int:node_id>", views.node_api, name="get_node_info"),
    path("nodes/online", views.node_online_api, name="post_onlineip"),
    path(
        "users/nodes/<int:node_id>", views.node_user_configs, name="node_user_configs"
    ),
    path("traffic/upload", views.TrafficReportView.as_view(), name="post_traffic"),
    path(
        "user_ss_config/<int:node_id>/",
        views.UserSSConfigView.as_view(),
        name="user_ss_config",
    ),
    # 支付
    path("orders", views.OrderView.as_view(), name="order"),
    path("callback/alipay", views.ailpay_callback, name="alipay_callback"),
    # user stats
    path(
        "user/stats/ref_chart", views.UserRefChartView.as_view(), name="user_ref_chart"
    ),
    path(
        "user/stats/traffic_chart",
        views.UserTrafficChartView.as_view(),
        name="user_traffic_chart",
    ),
]
