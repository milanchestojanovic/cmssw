# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --conditions auto:run2_data -s RAW2DIGI,L1Reco,RECO --process RECO -n 30 --data --era Run2_2018_pp_on_AA --eventcontent RECO --runUnscheduled --scenario HeavyIons --datatier RECO --repacked --python RECOHID18.py --no_exec --filein file:step1.root --fileout file:step2.root --nThreads 4
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2018_pp_on_AA)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContentHeavyIons_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_DataMapper_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
#process.load('RecoLocalTracker.SiPixelRecHits.SiPixelRecHitsMilan_cfi')
#process.load('newRecHitProducer.NewPixelHitPRoducer.newPixelRecHitPRoducer_cfi')
#process.load('RecoLocalTracker.SiStripRecHitConverter.SiStripClusters2ApproxClustersv2_cfi')
process.load('RecoLocalTracker.SiStripRecHitConverter.SiStripNewRecHitProducer_cfi')
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(3)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring( 
	#'file:/eos/cms/store/hidata/HIRun2018A/HIMinimumBias3/RAW/v1/000/326/569/00000/15221D80-0407-FD46-A096-FA0BBA25853E.root'
	'file:/eos/cms/store/hidata/HIRun2018A/HIMinimumBias5/RAW/v1/000/326/573/00000/C4CDB29C-62C9-AF4D-B2A3-5D9793BE3832.root'
	#'file:/afs/cern.ch/work/r/rxiao/public/raw_data_format_files/outputHIPhysicsMinimumBias5.root'
	#'file:/afs/cern.ch/work/r/rxiao/public/2021_raw_data_format_new/CMSSW_10_3_0_pre6/src/hlt/root_500_events/outputHIPhysicsMinimumBias5.root'
        #'file:/eos/user/m/mstojano/Run3/PbPb2018RAW/D14757DC-8433-464E-8092-0A8C2BA93DA1.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
   SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step3 nevts:30'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('RECO'),
        filterName = cms.untracked.string('')
    ),
    #outputCommands = cms.untracked.vstring('drop *','keep *_*_*_RecHit'),
    fileName = cms.untracked.string( 'file:/eos/user/m/mstojano/Run3/PbPb2018RAW/step2_test2021_alldef3evts.root'
    ),
    outputCommands = process.RECOEventContent.outputCommands,
    #splitLevel = cms.untracked.int32(0),
    compressionAlgorithm=cms.untracked.string("ZLIB"),
    compressionLevel=cms.untracked.int32(7)

)

process.RECOoutput.outputCommands = cms.untracked.vstring('keep *_*_*_*','drop *Photon*_*_*_*', 'drop *_*Photon*_*_*', 'drop *_*_*Photon*_*', 'drop *_*_*_*Photon*',
'drop *IsoDeposit*_*_*_*', 'drop *_*IsoDeposit*_*_*', 'drop *_*_*IsoDeposit*_*', 'drop *_*_*_*IsoDeposit*'
)
#process.RECOoutput.outputCommands = cms.untracked.vstring('drop *','keep recoTracks_generalTracks_*_*','keep *_siStripNewRecHitProducer_*_*','keep *_*SiStripClusters2ApproxClustersv2*_*_*','keep SiStripRecHit2DedmNewDetSetVector_siStripMatchedRecHits_stereoRecHit_RECO')

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_dataRun2_v6', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction*process.siStripNewRecHitProducer)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOoutput_step = cms.EndPath(process.RECOoutput)
#process.RECOoutput_step = cms.EndPath(process.RECOoutput*process.generalAndHiPixelTracks)
#process.RECOoutput_step = cms.EndPath(process.RECOoutput*process.siPixelRecHitsMilan)
#process.RECOoutput_step = cms.EndPath(process.RECOoutput*process.SiStripClusters2ApproxClustersv2)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.RECOoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(1)
process.options.numberOfStreams=cms.untracked.uint32(1)

from Configuration.Applications.ConfigBuilder import MassReplaceInputTag
MassReplaceInputTag(process, new="rawDataMapperByLabel", old="rawDataCollector")

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)


# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
