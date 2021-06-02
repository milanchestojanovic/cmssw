import FWCore.ParameterSet.Config as cms

siStripNewRecHitProducer = cms.EDProducer("SiStripNewRecHitProducer",
    inputClusters = cms.InputTag("siStripClusters"),
    src = cms.InputTag("siPixelClusters"),
    CPE = cms.string('PixelCPEGeneric'),
    inputHits = cms.InputTag('siStripMatchedRecHits','matchedRecHit'),
    VerboseLevel = cms.untracked.int32(1)

)

