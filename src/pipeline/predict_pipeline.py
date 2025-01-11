import os
import sys
import pandas as pd
from flask import Flask, request, render_template
from src.exception import CustomException
from src.utils import load_object




class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self,feature):
        try:
            model_path = os.path.join('artifacts','model.pkl')
            preprocess_path = os.path.join('artifacts','preprocessor.pkl')
            print('Before Loading...')
            model = load_object(model_path)
            preprocessor = load_object(preprocess_path)
            print('After Loading...')
            data_scaled = preprocessor.transform(feature)
            prediction = model.predict(data_scaled)
            if prediction==1:
                return 'Attack'
            elif prediction==0:
                return 'Normal'
        
        except Exception as e:
            raise CustomException(e,sys)


# CustomData class for handling input with additional features
class CustomData:
    def __init__(self, duration: float, protocol_type: str, service: str, flag: str,
                 src_bytes: int, dst_bytes: int, land: int, wrong_fragment: int,
                 urgent: int, hot: int, num_failed_logins: int, logged_in: int,
                 num_compromised: int, root_shell: int, su_attempted: int,
                 num_root: int, num_file_creations: int, num_shells: int,
                 num_access_files: int, num_outbound_cmds: int, is_host_login: int,
                 is_guest_login: int, count: int, srv_count: int, serror_rate: float,
                 srv_serror_rate: float, rerror_rate: float, srv_rerror_rate: float,
                 same_srv_rate: float, diff_srv_rate: float, srv_diff_host_rate: float,
                 dst_host_count: int, dst_host_srv_count: int,
                 dst_host_same_srv_rate: float, dst_host_diff_srv_rate: float,
                 dst_host_same_src_port_rate: float, dst_host_srv_diff_host_rate: float,
                 dst_host_serror_rate: float, dst_host_srv_serror_rate: float,
                 dst_host_rerror_rate: float, dst_host_srv_rerror_rate: float):
        """
        Initialize CustomData with user-provided input attributes.
        """
        self.duration = duration
        self.protocol_type = protocol_type
        self.service = service
        self.flag = flag
        self.src_bytes = src_bytes
        self.dst_bytes = dst_bytes
        self.land = land
        self.wrong_fragment = wrong_fragment
        self.urgent = urgent
        self.hot = hot
        self.num_failed_logins = num_failed_logins
        self.logged_in = logged_in
        self.num_compromised = num_compromised
        self.root_shell = root_shell
        self.su_attempted = su_attempted
        self.num_root = num_root
        self.num_file_creations = num_file_creations
        self.num_shells = num_shells
        self.num_access_files = num_access_files
        self.num_outbound_cmds = num_outbound_cmds
        self.is_host_login = is_host_login
        self.is_guest_login = is_guest_login
        self.count = count
        self.srv_count = srv_count
        self.serror_rate = serror_rate
        self.srv_serror_rate = srv_serror_rate
        self.rerror_rate = rerror_rate
        self.srv_rerror_rate = srv_rerror_rate
        self.same_srv_rate = same_srv_rate
        self.diff_srv_rate = diff_srv_rate
        self.srv_diff_host_rate = srv_diff_host_rate
        self.dst_host_count = dst_host_count
        self.dst_host_srv_count = dst_host_srv_count
        self.dst_host_same_srv_rate = dst_host_same_srv_rate
        self.dst_host_diff_srv_rate = dst_host_diff_srv_rate
        self.dst_host_same_src_port_rate = dst_host_same_src_port_rate
        self.dst_host_srv_diff_host_rate = dst_host_srv_diff_host_rate
        self.dst_host_serror_rate = dst_host_serror_rate
        self.dst_host_srv_serror_rate = dst_host_srv_serror_rate
        self.dst_host_rerror_rate = dst_host_rerror_rate
        self.dst_host_srv_rerror_rate = dst_host_srv_rerror_rate

        
    def to_dataframe(self):
        """
        Convert the user input data into a pandas DataFrame.
        Returns:
            pd.DataFrame: DataFrame containing the user input data.
        """
        try:
            input_data = {
                "duration": [self.duration],
                "protocol_type": [self.protocol_type],
                "service": [self.service],
                "flag": [self.flag],
                "src_bytes": [self.src_bytes],
                "dst_bytes": [self.dst_bytes],
                "land": [self.land],
                "wrong_fragment": [self.wrong_fragment],
                "urgent": [self.urgent],
                "hot": [self.hot],
                "num_failed_logins": [self.num_failed_logins],
                "logged_in": [self.logged_in],
                "num_compromised": [self.num_compromised],
                "root_shell": [self.root_shell],
                "su_attempted": [self.su_attempted],
                "num_root": [self.num_root],
                "num_file_creations": [self.num_file_creations],
                "num_shells": [self.num_shells],
                "num_access_files": [self.num_access_files],
                "num_outbound_cmds": [self.num_outbound_cmds],
                "is_host_login": [self.is_host_login],
                "is_guest_login": [self.is_guest_login],
                "count": [self.count],
                "srv_count": [self.srv_count],
                "serror_rate": [self.serror_rate],
                "srv_serror_rate": [self.srv_serror_rate],
                "rerror_rate": [self.rerror_rate],
                "srv_rerror_rate": [self.srv_rerror_rate],
                "same_srv_rate": [self.same_srv_rate],
                "diff_srv_rate": [self.diff_srv_rate],
                "srv_diff_host_rate": [self.srv_diff_host_rate],
                "dst_host_count": [self.dst_host_count],
                "dst_host_srv_count": [self.dst_host_srv_count],
                "dst_host_same_srv_rate": [self.dst_host_same_srv_rate],
                "dst_host_diff_srv_rate": [self.dst_host_diff_srv_rate],
                "dst_host_same_src_port_rate": [self.dst_host_same_src_port_rate],
                "dst_host_srv_diff_host_rate": [self.dst_host_srv_diff_host_rate],
                "dst_host_serror_rate": [self.dst_host_serror_rate],
                "dst_host_srv_serror_rate": [self.dst_host_srv_serror_rate],
                "dst_host_rerror_rate": [self.dst_host_rerror_rate],
                "dst_host_srv_rerror_rate": [self.dst_host_srv_rerror_rate],
            }
            data = pd.DataFrame(input_data)
            
            return data

        except Exception as e:
            raise CustomException(e, sys)

