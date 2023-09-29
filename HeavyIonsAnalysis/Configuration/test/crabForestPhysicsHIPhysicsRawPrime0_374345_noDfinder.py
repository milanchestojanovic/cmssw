from WMCore.Configuration import Configuration
#from CRABClient.UserUtilities import getUsername

config = Configuration()

inputList = 'fileListPhysicsHIPhysicsRawPrime0_374345.txt'
jobTag = "PbPb2023_run374345_PhysicsHIPhysicsRawPrime0_2023-09-29"
#username = getUsername()

config.section_("General")
config.General.requestName = jobTag
config.General.workArea = config.General.requestName
config.General.transferOutputs = True
config.General.transferLogs = False

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'forest_miniAOD_run3_DATA.py'
#config.JobType.inputFiles = 'emap_2023_newZDC_v3.txt'
config.JobType.maxMemoryMB = 2500
config.JobType.maxJobRuntimeMin = 600
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.userInputFiles = open(inputList).readlines()
config.Data.totalUnits = len(config.Data.userInputFiles)
#config.Data.inputDataset = '/Alternatively/DefineDataset/InsteadOf/InputFileList'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2  
config.Data.outLFNDirBase = '/store/group/phys_heavyions/mstojano/run3RapidValidation/' + config.General.requestName
config.Data.publication = False

config.section_("Site")
config.Site.whitelist = ['T2_US_*']
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.storageSite = 'T2_US_Purdue'
