#-*- encoding:utf-8 -*-

import json 

class FUZZPOST:
    
    def __init__(self):
        self.filepath = ''
        self.fuzzing_param_name = "{{fuzzParam}}"
        self.body_parameter_name_list = []
        
        self.switch_header = 0
        self.switch_method = 0
        self.switch_url = 0
        self.switch_body = 1
        
    def __del__(self):
        pass
    
    def get_config(self):
        select = input("fuzz method ? > (y/default:N)")
        if "y" == select.lower():
            self.switch_method = 1
            
        select = input("fuzz url ? > (y/default:N)")
        if "y" == select.lower():
            self.switch_url = 1
        
        select =input("fuzz header ? > (y/default:N)")
        if "y" == select.lower():
            self.switch_header = 1
        
        select =input("fuzz body ? > (default:Y/n)")
        if "y" == select.lower():
            self.switch_body = 1
            
        filepath = input(".json file path? >  ")
        self.filepath = filepath
        
        fuzzparam = input("fuzzparam variable name ? (default:{{fuzzParam}})\nex) {{vairable}}\nyou can default value, just input \"d\"  > ")
        if "d" == fuzzparam:
            self.fuzzing_param_name = "{{fuzzParam}}"
        else:
            self.fuzzing_param_name =  fuzzparam
        
    def set_config(self):
        data = ''
        with open(self.filepath, "r+") as f:
            data = f.read()
        self.postman_swagger = json.loads(data)

    def extract_json_key(self):
        # print(postman_swagger.keys())
        for i in self.postman_swagger.keys():
            
            if type(self.postman_swagger[i]) == type({}):
                # print(self.postman_swagger[i].keys())
                pass
            else:
                # print(self.postman_swagger[i].__len__())
                if self.postman_swagger[i].__len__() > 2:
                    for j in range(0,self.postman_swagger[i].__len__()):
                        # print(postman_swagger[i][j])
                        if type(self.postman_swagger[i][j]) == type({}):
                            # print(self.postman_swagger[i][j].keys())
                            print("[*] extract API name : " + self.postman_swagger[i][j]['name'])
                            # print("request : " + postman_swagger[i][j]['request'])
                            # print(self.postman_swagger[i][j]['request'].keys())
                            
                            if 'method' in self.postman_swagger[i][j]['request'].keys() and self.switch_method == 1:
                                print(self.postman_swagger[i][j]['request']['method'])

                            if 'header' in self.postman_swagger[i][j]['request'].keys() and self.switch_header == 1:
                                print(self.postman_swagger[i][j]['request']['header'])
                                # input()
                            
                            if 'body' in self.postman_swagger[i][j]['request'].keys() and self.switch_body == 1:
                                # print(postman_swagger[i][j]['request']['body'])
                                # print(type(postman_swagger[i][j]['request']['body']))
                                # print(postman_swagger[i][j]['request']['body'].keys())
                                if 'raw' == self.postman_swagger[i][j]['request']['body']['mode']:
                                    # print(postman_swagger[i][j]['request']['body']['raw'])
                                    raw_loads = json.loads(self.postman_swagger[i][j]['request']['body']['raw'])
                                    # print(raw_loads.keys())
                                    for k in raw_loads.keys():
                                        self.body_parameter_name_list.append(k)
                                else:
                                    print(f"다른 body 모드 입니다. : {self.postman_swagger[i][j]['request']['body']['mode']}")
                        else:
                            pass
                        self.body_parameter_name_list = list(set(self.body_parameter_name_list))
                else:
                    for j in range(0,self.postman_swagger[i].__len__()):
                        pass
                        # print(self.postman_swagger[i][j])

        print(f"[*] target_parameter_list : {self.body_parameter_name_list}")
        input("> Enter")
    
    def set_fuzz_param(self):
        for i in self.postman_swagger.keys():
            if type(self.postman_swagger[i]) == type({}):
                # print(self.postman_swagger[i].keys())
                pass
            else:
                # print(self.postman_swagger[i].__len__())
                if self.postman_swagger[i].__len__() > 2:
                    for j in range(0,self.postman_swagger[i].__len__()):
                        # print(postman_swagger[i][j])
                        if type(self.postman_swagger[i][j]) == type({}):
                            # print(self.postman_swagger[i][j].keys())
                            print("[*] Set Fuzzning Variable at : " + self.postman_swagger[i][j]['name'])
                            # print("request : " + postman_swagger[i][j]['request'])
                            # print(self.postman_swagger[i][j]['request'].keys())
                            if 'method' in self.postman_swagger[i][j]['request'].keys() and self.switch_method == 1:
                                print(self.postman_swagger[i][j]['request']['method'])

                            if 'header' in self.postman_swagger[i][j]['request'].keys() and self.switch_header == 1:
                                print(self.postman_swagger[i][j]['request']['header'])
                            
                            if 'body' in self.postman_swagger[i][j]['request'].keys() and self.switch_body == 1:
                                # print(postman_swagger[i][j]['request']['body'])
                                # print(type(postman_swagger[i][j]['request']['body']))
                                # print(postman_swagger[i][j]['request']['body'].keys())
                                if 'raw' == self.postman_swagger[i][j]['request']['body']['mode']:
                                    # print(postman_swagger[i][j]['request']['body']['raw'])
                                    raw_loads = json.loads(self.postman_swagger[i][j]['request']['body']['raw'])
                                    # print(raw_loads.keys())
                                    for k in raw_loads.keys():
                                        if k in self.body_parameter_name_list:
                                            raw_loads[k] = self.fuzzing_param_name
                                            # print(f"└ {k} : {self.fuzzing_param_name}")
                                    raw_dumps = json.dumps(raw_loads)
                                    self.postman_swagger[i][j]['request']['body']['raw'] = raw_dumps
                                    # print(f"postman_swagger[i][j]['request']['body']['raw'] : {self.postman_swagger[i][j]['request']['body']['raw']}")
                                else:
                                    print(f"다른 body 모드 입니다. : {self.postman_swagger[i][j]['request']['body']['mode']}")
                        else:
                            pass
                        self.body_parameter_name_list = list(set(self.body_parameter_name_list))
                        # print(f"body_parameter_name_list : {body_parameter_name_list}")
                        # input()
                else:
                    for j in range(0,self.postman_swagger[i].__len__()):
                        pass
                        # print(self.postman_swagger[i][j])
                #print(type(postman_swagger[i]))
        save_filepath = self.filepath.replace(".json","_fuzz.json")
        try:
            with open(save_filepath, "w+", encoding="utf-8") as f:
                f.write(json.dumps(self.postman_swagger, sort_keys=True, indent=4))
            print(f"[*] saved {save_filepath}")
        except Exception as e:
            print(f"[*] save error - {e}")
            
if __name__ == "__main__":
    fuzzpost = FUZZPOST()
    
    fuzzpost.get_config()
    fuzzpost.set_config()
    fuzzpost.extract_json_key()
    fuzzpost.set_fuzz_param()