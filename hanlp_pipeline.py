import hanlp
segment_dict = {'急性肠胃炎', '盛剑环境'}
my_project_name = "hanlp的pipeline使用测试"

# 自定义一个函数
def custom_function(input_list, pro_name):
    return {
        'my_project_name': f"项目的名称为：{pro_name}",
        'raw_input': input_list  # 返回原始输入
    }

def segment(input_list, seg_dict):
    Segment = hanlp.load('CTB9_TOK_ELECTRA_SMALL')
    Segment.dict_force = None
    Segment.dict_combine = seg_dict
    
    # 获取原始输入
    raw_input = input_list['raw_input']
    segment_result = Segment(raw_input)
    return segment_result

HanLP = hanlp.pipeline() \
    .append(custom_function, output_key='custom_function_result', pro_name=my_project_name)\
    .append(segment, output_key='tok', input_key='custom_function_result', seg_dict=segment_dict)

doc = HanLP(['急性肠胃炎要如何治疗？', '盛剑环境的股价太高了。'])
print(doc)
print(doc["custom_function_result"]["my_project_name"])