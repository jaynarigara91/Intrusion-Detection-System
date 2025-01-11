import streamlit as st
import pandas as pd
import numpy as np  
from src.pipeline.predict_pipeline import PredictPipeline

input_data = {}

columns = [
        "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
        "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
        "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations",
        "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login",
        "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
        "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate",
        "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
        "dst_host_same_srv_rate", "dst_host_diff_srv_rate", 
        "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
        "dst_host_serror_rate", "dst_host_srv_serror_rate", 
        "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "labels"
    ]

    # Define the categorical options
services = ['smtp', 'domain_u', 'other', 'private', 'http', 'ecr_i', 'mtp',
            'netstat', 'http_443', 'uucp_path', 'eco_i', 'imap4', 'ldap',
            'Z39_50', 'discard', 'csnet_ns', 'pop_3', 'ftp_data', 'klogin',
            'finger', 'courier', 'auth', 'systat', 'supdup', 'telnet',
            'iso_tsap', 'ssh', 'ftp', 'exec', 'netbios_ssn', 'whois',
            'netbios_ns', 'domain', 'urp_i', 'uucp', 'pop_2', 'nntp', 'kshell',
            'time', 'ctf', 'efs', 'IRC', 'nnsp', 'sunrpc', 'ntp_u', 'bgp',
            'gopher', 'hostnames', 'daytime', 'link', 'sql_net', 'echo', 'X11',
            'netbios_dgm', 'shell', 'vmnet', 'name', 'remote_job', 'login',
            'printer', 'pm_dump', 'rje', 'red_i', 'tim_i', 'urh_i', 'aol',
            'http_8001', 'http_2784', 'tftp_u', 'harvest']

flags = ['SF', 'RSTR', 'S0', 'REJ', 'SH', 'RSTO', 'S3', 'OTH', 'S1', 'S2', 'RSTOS0']

protocol_types = ['tcp', 'udp', 'icmp']

st.title("Intrusion Detection System")   

# Create input fields based on the column types
for column in columns:
    if column == "service":
        input_data[column] = st.selectbox(f"Select value for {column}", services)
    elif column == "flag":
        input_data[column] = st.selectbox(f"Select value for {column}", flags)
    elif column == "protocol_type":
        input_data[column] = st.selectbox(f"Select value for {column}", protocol_types)
    else:
        input_data[column] = st.text_input(f"Enter value for {column}")



data = pd.DataFrame([input_data])
print(data)
if st.button("Prediction"):    
    Predict_pipeline = PredictPipeline(data)
    print("Wait Pedicting....")
    result = Predict_pipeline.predict(data)
    if result==0:
        st.success("Normal")
    elif result==1:
        st.success("Attack")