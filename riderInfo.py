from xbtFunctions import *

class RiderClass:
  def __init__(self, name, email, institution, phone):
    self.name = name
    self.email = email
    self.institution = institution
    self.phone = phone


def get_rider_info(StringOfBits,csvList,newMessageType,dataPoints):

    rider = RiderClass("name", "email", "institution", "phone")

    # Temperature blocks info (size, start, end)
    [SSTstartBit,SSTendBit] = get_range(csvList, "SEA_SURFACE_TEMPERATURE", newMessageType)
    [tempStartBit,tempEndBit] = get_range(csvList, "RIDER_NAME", newMessageType)
    blockSize = SSTendBit - SSTstartBit + 1
    # print("SSTstartBit:",SSTstartBit,"tempStartBit:",tempStartBit,"blockSize:",blockSize)

    # 1- rider name
    [a,b] = get_range(csvList, "NUMBER_OF_RIDER_BLOCKS", newMessageType)
    riderBlocks = int(bits_to_dec(StringOfBits,a,b,1,0))
    riderNameStartBit = tempStartBit + dataPoints * blockSize -1 # adjusted to python indexing [0,n+1] to get complete array
    riderNameEndBit = riderNameStartBit + riderBlocks * 40 
    rider.name = bits_to_ascii(StringOfBits,riderNameStartBit,riderNameEndBit)
    
    # 2- rider email
    [a,b] = get_range(csvList, "NUMBER_OF_RIDER_EMAIL_BLOCKS", newMessageType)
    riderEmailBlocks = int(bits_to_dec(StringOfBits,a,b,1,0))
    riderEmailStartBit = riderNameEndBit 
    riderEmailEndBit = riderEmailStartBit + riderEmailBlocks * 40
    rider.email = bits_to_ascii(StringOfBits,riderEmailStartBit,riderEmailEndBit)
 
    # 3- rider institution
    [a,b] = get_range(csvList, "NUMBER_OF_RIDER_INSTITUTION_BLOCKS", newMessageType)
    riderInstitutionBlocks = int(bits_to_dec(StringOfBits,a,b,1,0))
    riderInstitutionStartBit = riderEmailEndBit 
    riderInstitutionEndBit = riderInstitutionStartBit + riderInstitutionBlocks * 40 
    rider.institution = bits_to_ascii(StringOfBits,riderInstitutionStartBit,riderInstitutionEndBit)

    # 4- rider phone
    [a,b] = get_range(csvList, "NUMBER_OF_RIDER_PHONE_BLOCKS", newMessageType)
    riderPhoneBlocks = int(bits_to_dec(StringOfBits,a,b,1,0))
    riderPhoneStartBit = riderInstitutionEndBit 
    riderPhoneEndBit = riderPhoneStartBit + riderPhoneBlocks * 40 
    rider.phone = bits_to_ascii(StringOfBits,riderPhoneStartBit,riderPhoneEndBit)

    return rider