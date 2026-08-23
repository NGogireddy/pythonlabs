import json
from exceptions import InvalidSensorDataError, InvalidQuantumReadingError


DIVIDER_LINE = '========================================'
HEADING = ' Quantum Sensor Processing Report '
UNDER_LINE = '-------------'
COMPLETED_STATUS = 'Processing Status: COMPLETED'


# review of Valid_schema function
def valid_schema(schema):
    """
    Validates if the schema is a valid quantum schema for correct keys
    :param schema:
    :return: bool
    :raises: InvalidSensorDataError
    """

    if "device_id" in schema and "backend" in schema and "readings" in schema:
        if isinstance(schema["readings"], list):
            return True
    raise InvalidSensorDataError(schema)


"""
-   What should it receive?
    Input: I should receive a json schema. Not a string or anything else. 
    
-   What should it return?
    Output: Return True if the schema is as per the design i.e, have the valid keys in it.
    
-   Should it raise an exception?
    Yes, it should raise custom exception if the schema is not according to the business requirements. 
    
-   Should it print anything?
    No nothing required. 
    
-   Should it access the filesystem?
    No, not required. 
    
-   Should it modify global state?
    No, no modifications required. 

Conclusion: 
The above method is sticking to the fundamentals, no changes are required. 
"""


# review of valid_reading function
def valid_reading(reading):
    """
    Validate if the reading is between 0 and 1
    :param reading: string
    :return: float(reading)
    :raises: InvalidQuantumReadingError
    """
    try:
        value = float(reading)
        if 0 <= value <= 1:
            return value**2
        raise InvalidQuantumReadingError(f"Out of boundary")
    except (ValueError, TypeError):
        raise InvalidQuantumReadingError("Invalid Value")


"""
-   What should it receive?
    Input: It should receive a sensor reading. 
    
-   What should it return?
    Output: True if the reading is a number between 0 and 1. 
    
-   Should it raise an exception?
    Yes: If the received input is not a number and if the number is out of bounds [0,1] raise a custom exception
    
-   Should it print anything?
    No, it shouldn't print anything. 
    
-   Should it access the filesystem?
    No, file access is needed for this. 
    
-   Should it modify global state?
    No, it should not modify any global state. 

Conclusion: 
The above method is validating and raising correct exceptions but returning squared values, it should ideally return 
a boolean value. This method should be re-written as below.  
"""


def updated_valid_reading(reading):
    """
    Validate if the reading is between 0 and 1
    :param reading: string
    :return: float
    :raises: InvalidQuantumReadingError
    """
    try:
        value = float(reading)
    except (ValueError, TypeError):
        raise InvalidQuantumReadingError("Invalid Value")
    if 0 <= value <= 1:
        return value
    raise InvalidQuantumReadingError(f"Out of boundary")


# review of process_readings function
def process_readings(sensor_readings):
    """
    Square the readings and return
    :param sensor_readings:
    :return: A list of squared readings if valid value otherwise reason for invalid value
    """
    output = []
    for reading in sensor_readings:
        try:
            output.append(valid_reading(reading))
        except InvalidQuantumReadingError as e:
            output.append(e.message)
    return output


"""
-   What should it receive?
    Input: It should receive a valid json schema verified for business rules i.e having all correct keys
    
-   What should it return?
    Output: It should return a dictionary of the report. 
    
-   Should it raise an exception?
    Yes, if the readings is not a list, it should raise a ValueError exception. 
    
-   Should it print anything?
    No, it will not print anything. 
    
-   Should it access the filesystem?
    No access to the file system required. 
    
-   Should it modify global state?
    No modifications to the file system. 
    
Conclusion: 
The scope of the above function is changed and will be re-written as below. 
"""


def updated_process_reading(sensor_reading):
    """
    Sensor readings have all the keys, square the valid values and return the report.
    :param sensor_reading: JSON schema of sensor reading.
    :return: A report of the processed JSON data.
    """
    output = {"device_id": sensor_reading["device_id"],
              "backend": sensor_reading["backend"],
              "total_readings": len(sensor_reading["readings"]),
              "valid_readings": [],
              "invalid_readings": []}

    for reading in sensor_reading["readings"]:
        try:
            output["valid_readings"].append((reading, updated_valid_reading(reading) ** 2))
        except InvalidQuantumReadingError as e:
            output["invalid_readings"].append((reading, e.message))
    return output


# generate_report function
"""
generate_report is not defined in the original week2 capstone project writing it new.

-   What should it receive?
    Input: It receives the dictionary to generate the summary report
     
-   What should it return?
    Output: It will not return anything. 
    
-   Should it raise an exception?
    Ideally it need not raise any exception. I want to see if any runtime Errors are raised whilst testing it. 
     
-   Should it print anything?
    Yes, the main goal of this function is to generate a report. 
    
-   Should it access the filesystem?
    No, it will not write anything to the files. 
    
-   Should it modify global state?
    No changes to the global state. 
    
"""


def generate_report(report):
    """
    Receives processed sensor data and generates a report.
    :param report: Processed sensor data
    :return: None
    """
    if report is not None:
        print(DIVIDER_LINE)
        print(HEADING)
        print(DIVIDER_LINE + "\n")
        print(f'{"Device ID":16} : {report["device_id"]}')
        print(f'{"Backend":16} : {report["backend"]} \n')
        print(f'{"Total readings":16} : {report["total_readings"]}')
        print(f'{"Valid readings":16} : {len(report["valid_readings"])}')
        print(f'{"Invalid readings":16} : {len(report["invalid_readings"])}\n')
        print('Valid results')
        print(UNDER_LINE)
        for value, output in report["valid_readings"]:
            print(f'{str(value):6} -> {output}')
        print("")
        print('Invalid results')
        print(UNDER_LINE)
        for value, output in report["invalid_readings"]:
            print(f'{str(value):6} -> {output}')
        print("")
        print(COMPLETED_STATUS)
        print(DIVIDER_LINE)


# load_sensor_data function
"""
load_sensor_data is not defined in the original week2 capstone project writing it new.

-   What should it receive?
    Input: file path to load sensor data

-   What should it return?
    Output: Return the data read from the file path 

-   Should it raise an exception?
    Yes, FileNotFoundError

-   Should it print anything?
    Yes, the main goal of this function is to generate a report. 

-   Should it access the filesystem?
    No, it will not write anything to the files. 

-   Should it modify global state?
    No changes to the global state. 

"""


def load_sensor_data(file_path):
    """
    read data from path and return it
    :param file_path: Input file path where sensor data is stored
    :return: content of the file
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No file in the path: {file_path}")
    except json.JSONDecodeError as e:
        raise InvalidSensorDataError(f"File at {file_path} contains invalid JSON syntax ({e.msg})")
    return data
