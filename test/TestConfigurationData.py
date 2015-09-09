
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
from cp3_llbb.Framework import Framework

process = Framework.create(eras.Run2_50ns, '74X_dataRun2_Prompt_v1')

process.framework.analyzers.dilepton = cms.PSet(
        type = cms.string('dilepton_analyzer'),
        prefix = cms.string('dilepton_'),
        enable = cms.bool(True)
        )

process.framework.analyzers.test = cms.PSet(
        type = cms.string('test_analyzer'),
        prefix = cms.string('test_'),
        enable = cms.bool(True)
        )

Framework.schedule(process, ['dilepton', 'test'])

process.source.fileNames = cms.untracked.vstring(
        '/store/data/Run2015B/DoubleMuon/MINIAOD/17Jul2015-v1/30000/D8ED75E7-C12E-E511-8CBF-0025905A608C.root'
        )