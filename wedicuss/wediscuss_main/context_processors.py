from wediscuss_main.models import Discuss_group
#context processor
def discuss_group(request):
    # group_list = Discuss_group.get_jioned_group_list(request)
    # group_info = Discuss_group.get_sel_group_info(request)
    ctx = {
        "GROUP_LIST":Discuss_group.get_jioned_group_list(request),
        # "GROUP_INFO":Discuss_group.get_sel_group_info(request),
    }
    return ctx


#function

