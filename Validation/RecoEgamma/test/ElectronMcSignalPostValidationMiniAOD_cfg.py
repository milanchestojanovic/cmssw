
import sys
import os
import FWCore.ParameterSet.Config as cms

from electronValidationCheck_Env import env
cmsEnv = env() # be careful, cmsEnv != cmsenv. cmsEnv is local

cmsEnv.checkSample() # check the sample value
cmsEnv.checkValues()

if cmsEnv.beginTag() == 'Run2_2017':
    from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
    process = cms.Process("electronPostValidation",Run2_2017)
elif cmsEnv.beginTag() == 'Run3':
    from Configuration.Eras.Era_Run3_cff import Run3
    process = cms.Process('electronPostValidation', Run3) 
else:
    from Configuration.Eras.Era_Phase2_cff import Phase2
    process = cms.Process('electronPostValidation',Phase2)

#process.options = cms.untracked.PSet( )

process.DQMStore = cms.Service("DQMStore")
process.load("Validation.RecoEgamma.ElectronMcSignalPostValidatorMiniAOD_cfi")
process.load("DQMServices.Components.DQMStoreStats_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
# load DQM
process.load("DQMServices.Core.DQM_cfg")
process.load("DQMServices.Components.DQMEnvironment_cfi")
process.load("Configuration.StandardSequences.EDMtoMEAtJobEnd_cff")
# import DQMStore service
process.load('DQMOffline.Configuration.DQMOffline_cff')

# actually read in the DQM root file
process.load("DQMServices.Components.DQMFileReader_cfi")

# others
# import of standard configurations
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D76Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DQMSaverAtRunEnd_cff')
process.load('Configuration.StandardSequences.Harvesting_cff')


from DQMServices.Components.DQMStoreStats_cfi import *
dqmStoreStats.runOnEndJob = cms.untracked.bool(True)

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))

print('= inputPostFile : %s' % os.environ['inputPostFile'])
t1 = os.environ['inputPostFile'].split('.')
localFileInput = os.environ['inputPostFile']#.replace(".root", "_a.root") #
# Source
process.source = cms.Source ("PoolSource",fileNames = cms.untracked.vstring("file:" + localFileInput),
secondaryFileNames = cms.untracked.vstring(),)

process.electronMcSignalPostValidatorMiniAOD.InputFolderName = cms.string("EgammaV/ElectronMcSignalValidatorMiniAOD")
process.electronMcSignalPostValidatorMiniAOD.OutputFolderName = cms.string("EgammaV/ElectronMcSignalValidatorMiniAOD")

from Configuration.AlCa.autoCond import autoCond
#process.GlobalTag.globaltag = os.environ['TEST_GLOBAL_TAG']#+'::All'
process.GlobalTag.globaltag = '122X_mcRun4_realistic_v1'
#process.GlobalTag.globaltag = '113X_mcRun4_realistic_v4'
#process.GlobalTag.globaltag = '93X_mc2017_realistic_v1'

process.dqmSaver.workflow = '/electronHistos/' + t1[1] + '/RECO3'
process.dqmsave_step = cms.Path(process.DQMSaver)

process.p = cms.Path(process.EDMtoME * process.electronMcSignalPostValidatorMiniAOD * process.dqmStoreStats)

# Schedule
process.schedule = cms.Schedule(
                                process.p,
                                process.dqmsave_step,
)