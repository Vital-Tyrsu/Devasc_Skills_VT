# RESTCONF Automation

## Task Overview

This task involves creating a Python script to interact with a Cisco IOS device using RESTCONF, based on provided curl command examples. The task requires testing and transforming three curl commands into RESTCONF requests. Additionally, there is a provision for a quick fix to activate "logging monitor" using the Cisco IOS CLI in case of errors. Screenshots indicating the success of the actions need to be captured, and the Python code should be saved on GitHub.

## Task Phases

### Task Preparation

1. **Environment Setup:**
   - Ensure that the virtual DEVASC machine and the virtual CSR1Kv router are running and accessible.

2. **Python Libraries Installation:**
   - Install the necessary Python libraries for RESTCONF. You may use libraries such as `requests`.
     ```bash
     pip install requests
     ```

### Task Implementation

3. **Python Script:**
   - Create 3 Python scripts to transform curl commands into RESTCONF requests.

4. **Execution and Verification:**
   - Run the Python script and capture screenshots indicating the success of the actions.
   - Verify that the RESTCONF interactions and the logging activation were successful.

5. **Save Code on GitHub:**
   - Save the Python code on GitHub for future reference.

## Task Troubleshooting

6. **Error Handling:**
   - If errors occur during script execution, troubleshoot by checking the responses and adapting the code accordingly.
   - Ensure that the virtual CSR1Kv router is reachable and that RESTCONF is properly configured.

7. **Debugging:**
   - Utilize Python's `print` statements or debugging tools to identify and address any issues.
   - Refer to the RESTCONF Protocol documentation for troubleshooting tips.

## Notes

Adjust the steps based on your specific environment and requirements. This README provides a structured approach for the task.

