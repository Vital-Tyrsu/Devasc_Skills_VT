# Ansible 

## Task Overview

This Ansible playbook automates the task of configuring the logging buffer size to 5000 bytes on a Cisco IOS device.

## Task Phases

### Task Name
- Set Logging Buffer Size

### Task Preparation

1. **Inventory Configuration:**
   - Ensure that the target host is defined in the Ansible inventory file.

2. **Ansible Collection Installation:**
   - Install the `cisco.ios` collection on the Ansible control machine.
   - (ansible-galaxy collection install cisco.ios)

### Task Implementation

3. **Ansible Playbook:**
   - Create an Ansible playbook (`IOS_Facts.yaml`):
     ```yaml
     ---
     - name: run multiple commands on remote nodes
      ios_command:
        commands:
          - show version
          - show interfaces
      register: ios_version_output

     - name: Set Logging Buffer Size
       hosts: your_target_hosts
       gather_facts: False
       tasks:
         - name: Configure logging buffer size
           ios_config:
             lines:
               - logging buffered 5000
           become: yes
           become_method: enable
     ```
   - Replace `your_target_hosts` with the actual host or group in your inventory.

4. **Run Ansible Playbook:**
   - Execute the playbook using the `ansible-playbook` command:
     ```bash
     ansible-playbook IOS_Facts.yaml
     ```

### Task Troubleshooting

5. **Error Handling:**
   - Monitor the playbook execution for any errors.
   - Verify that the target device is reachable and that Ansible has the necessary permissions.

6. **Debugging:**
   - Use Ansible's `debug` module to print debug information if needed.
   - Check the Ansible execution output for any error messages.

### Task Verification

7. **Verification Steps:**
   - Verify the logging buffer size on the Cisco IOS device using the `show logging` or `show running-config` command.
   - Confirm that the size is set to 5000 bytes.

8. **Log Analysis:**
   - Check the logs or output of the Ansible playbook for any reported changes or success messages.

9. **Logging Buffer Verification:**
   - Log in to the Cisco IOS device manually and verify the configured logging buffer size.
   - Confirm that the change matches the intended size (5000 bytes).

10. **Post-Verification Checks:**
    - Ensure that the logging functionality continues to work as expected after the configuration change.

## Notes

Adjust the steps based on your specific environment and requirements. This README by Vital Tyrsu provides a structured approach for the task.
