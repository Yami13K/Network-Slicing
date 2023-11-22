import os
import sys

results_dir = os.path.join(sys.path[0],
                           'run_rl_just_on_rush_hours')
centralized_weights = os.path.join(results_dir, 'centralized_weights')
decentralized_weights = os.path.join(results_dir, 'decentralized_weights')
path_memory_centralize = os.path.join(results_dir, 'centralize_memory')
path_memory_decentralize = os.path.join(results_dir, 'decentralize_memory')
# prev_results_dir = "//content//drive//MyDrive//network_slicing//prev_results//"
utility_requested_ensured_path = os.path.join(results_dir, 'utility_requested_ensured')
reward_decentralized_path = os.path.join(results_dir, 'reward_decentralized')
reward_accumilated_decentralize_path = os.path.join(results_dir, 'reward_accumilated_decentralize')
reward_centralized_path = os.path.join(results_dir, 'reward_centralized')
reward_320_decentralized_path = os.path.join(results_dir, 'reward_320_decentralized')
qvalue_decentralized_path = os.path.join(results_dir, 'qvalue_decentralized')
qvalue_centralized_path = os.path.join(results_dir, 'qvalue_centralized')
requested_decentralized_path = os.path.join(results_dir, 'requested_decentralized')
ensured_decentralized_path = os.path.join(results_dir, 'ensured_decentralized')
available_capacity_decentralized_path = os.path.join(results_dir, 'available_capacity_decentralized')
action_decentralized_path = os.path.join(results_dir, 'action_decentralized')
supported_service_decentralized_path = os.path.join(results_dir, 'supported_service_decentralized')
waiting_buffer_length_path = os.path.join(results_dir, "waiting_buffer_length")
timed_out_length_path = os.path.join(results_dir, "timed_out_length")
from_waiting_to_serv_length_path = os.path.join(results_dir, "from_waiting_to_serv_length")
wasting_req_length_path = os.path.join(results_dir, "wasting_req_length")
prev_results_3tanh_dir =f"{os.path.join(sys.path[0])}//results3_tanh//results3_tanh//"

    #"/content/drive/MyDrive/results3_tanh/results3_tanh"
    #f"{os.path.join(sys.path[0])}//results3_tanh//results3_tanh//"
#
utility_decentralized_path = os.path.join(results_dir, 'utility_decentralized')
sum_power_allocation_path = os.path.join(results_dir, "sum_power_allocation//")

prev_results_dec_weight = f"{os.path.join(sys.path[0])}/"
# prev_results_dec_memory = f"{os.path.join(sys.path[0])}//action_each_single_request_reward_method4_add_init_10_11_12_no_protrization_less_failure_less_reward//"
prev_centralize_weights_path = os.path.join(prev_results_3tanh_dir, "centralized_weights//")
# prev_decentralize_weights_path = os.path.join(prev_results_dec_weight, "fair_memory_selection_0.5_m0.5_m1_10/decentralized_weights/")
# prev_centralize_memory_path = os.path.join(prev_results_4tanh_dir,"centralize_memory//")
# prev_decentralize_memory_path = os.path.join(prev_results_dec_memory,"decentralize_memory//")
centralize_qvalue_path = os.path.join(results_dir, "qvalue_centralized_for_plotting//")
decentralize_qvalue_path = os.path.join(results_dir, "qvalue_decentralized_for_plotting//")
ratio_of_occupancy_decentralized_path = os.path.join(results_dir, "ratio_of_occupancy_decentralized//")
requests_with_execution_time_path = os.path.join(results_dir, "requests_with_execution_time//")
requests_with_out_time_path = os.path.join(results_dir, "requests_with_execution_time//")
timed_out_requests_over_the_simulation_path = os.path.join(results_dir, "timed_out_requests_over_the_simulation//")
from_wait_to_serve_requests_over_the_simulation_path = os.path.join(results_dir,
                                                                    "from_wait_to_serve_requests_over_the_simulation//")
generated_requests_over_simulation_path = os.path.join(results_dir, "generated_requests_over_simulation//")
delay_time_path = os.path.join(results_dir, "delay_time//")
request_info = os.path.join(results_dir, "request_info//")
number_of_timed_out_requests_from_algorithm_path = os.path.join(results_dir,
                                                                "number_of_timed_out_requests_from_algorithm//")
number_of_rejected_requests_over_simulation_path = os.path.join(results_dir,
                                                                "number_of_rejected_requests_over_simulation//")
sum_of_cost_of_all_rejected_requests_path = os.path.join(results_dir, "sum_of_cost_of_all_rejected_requests//")
number_of_abort_requests_over_the_simulation_path = os.path.join(results_dir,"number_of_abort_requests_over_the_simulation//")
users_logging_info_path = os.path.join(results_dir,"users_logging_info//")
reward_info_path = os.path.join(results_dir,"reward_info//")
states_of_memory_path =  os.path.join(results_dir,"states_of_memory//")

os.makedirs(states_of_memory_path,exist_ok=True)
os.makedirs(reward_info_path , exist_ok=True)
os.makedirs(users_logging_info_path , exist_ok=True)
os.makedirs(number_of_abort_requests_over_the_simulation_path,exist_ok=True)
os.makedirs(number_of_rejected_requests_over_simulation_path, exist_ok=True)
os.makedirs(sum_of_cost_of_all_rejected_requests_path, exist_ok=True)
os.makedirs(request_info, exist_ok=True)
os.makedirs(number_of_timed_out_requests_from_algorithm_path, exist_ok=True)
os.makedirs(delay_time_path, exist_ok=True)
os.makedirs(generated_requests_over_simulation_path, exist_ok=True)
os.makedirs(timed_out_requests_over_the_simulation_path, exist_ok=True)
os.makedirs(from_wait_to_serve_requests_over_the_simulation_path, exist_ok=True)
os.makedirs(requests_with_execution_time_path, exist_ok=True)
os.makedirs(requests_with_out_time_path, exist_ok=True)
os.makedirs(ratio_of_occupancy_decentralized_path, exist_ok=True)
os.makedirs(utility_requested_ensured_path, exist_ok=True)
os.makedirs(reward_decentralized_path, exist_ok=True)
os.makedirs(reward_320_decentralized_path, exist_ok=True)
os.makedirs(reward_centralized_path, exist_ok=True)
os.makedirs(qvalue_decentralized_path, exist_ok=True)
os.makedirs(qvalue_centralized_path, exist_ok=True)
os.makedirs(centralized_weights, exist_ok=True)
os.makedirs(decentralized_weights, exist_ok=True)
os.makedirs(path_memory_centralize, exist_ok=True)
os.makedirs(path_memory_decentralize, exist_ok=True)
os.makedirs(centralize_qvalue_path, exist_ok=True)
os.makedirs(decentralize_qvalue_path, exist_ok=True)
os.makedirs(requested_decentralized_path, exist_ok=True)
os.makedirs(ensured_decentralized_path, exist_ok=True)
os.makedirs(available_capacity_decentralized_path, exist_ok=True)
os.makedirs(action_decentralized_path, exist_ok=True)
os.makedirs(supported_service_decentralized_path, exist_ok=True)
os.makedirs(utility_decentralized_path, exist_ok=True)
os.makedirs(reward_accumilated_decentralize_path, exist_ok=True)
os.makedirs(sum_power_allocation_path, exist_ok=True)
os.makedirs(waiting_buffer_length_path, exist_ok=True)
os.makedirs(timed_out_length_path, exist_ok=True)
os.makedirs(from_waiting_to_serv_length_path, exist_ok=True)
os.makedirs(wasting_req_length_path, exist_ok=True)
