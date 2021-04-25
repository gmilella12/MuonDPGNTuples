import CRABClient
from WMCore.Configuration import Configuration 

config = Configuration()

config.section_("General")
config.General.requestName = 'GEMMuonNTuplizerOverMC'
config.General.workArea = "/afs/cern.ch/user/f/fivone/Documents/NTuplizerMC/CMSSW_11_2_4/src/MuDPGAnalysis"
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/user/f/fivone/Documents/NTuplizerMC/CMSSW_11_2_4/src/MuDPGAnalysis/MuonDPGNtuples/test/muDpgNtuples_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.pyCfgParams = ['isMC=False','nEvents=-1']

config.section_("Data")
config.Data.inputDataset = '/ExpressCosmics/Commissioning2021-Express-v1/FEVT'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 180
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/fivone/GEMMuonNtuplizerZmumu'
config.Data.outputDatasetTag = 'MWGR3_properLatencyOnGEM'
config.Data.runRange = '341343'

config.section_("Site")
config.Site.storageSite = 'T2_DE_RWTH'

config.section_("User")
config.User.voGroup = 'dcms'
