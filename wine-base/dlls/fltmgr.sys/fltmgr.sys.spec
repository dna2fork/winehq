@ stdcall FltAcquirePushLockExclusive(ptr)
@ stub FltAcquirePushLockShared
@ stub FltAcquireResourceExclusive
@ stub FltAcquireResourceShared
@ stub FltAllocateCallbackData
@ stub FltAllocateContext
@ stub FltAllocateDeferredIoWorkItem
@ stub FltAllocateFileLock
@ stub FltAllocateGenericWorkItem
@ stub FltAllocatePoolAlignedWithTag
@ stub FltAttachVolume
@ stub FltAttachVolumeAtAltitude
@ stub FltBuildDefaultSecurityDescriptor
@ stub FltCancelFileOpen
@ stub FltCancelIo
@ stub FltCbdqDisable
@ stub FltCbdqEnable
@ stub FltCbdqInitialize
@ stub FltCbdqInsertIo
@ stub FltCbdqRemoveIo
@ stub FltCbdqRemoveNextIo
@ stub FltCheckAndGrowNameControl
@ stub FltCheckLockForReadAccess
@ stub FltCheckLockForWriteAccess
@ stub FltCheckOplock
@ stub FltClearCallbackDataDirty
@ stub FltClearCancelCompletion
@ stub FltClose
@ stub FltCloseClientPort
@ stub FltCloseCommunicationPort
@ stub FltCompareInstanceAltitudes
@ stub FltCompletePendedPostOperation
@ stub FltCompletePendedPreOperation
@ stub FltCreateCommunicationPort
@ stub FltCreateFile
@ stub FltCreateFileEx
@ stub FltCreateSystemVolumeInformationFolder
@ stub FltCurrentBatchOplock
@ stub FltDecodeParameters
@ stub FltDeleteContext
@ stub FltDeleteFileContext
@ stub FltDeleteInstanceContext
@ stdcall FltDeletePushLock(ptr)
@ stub FltDeleteStreamContext
@ stub FltDeleteStreamHandleContext
@ stub FltDeleteVolumeContext
@ stub FltDetachVolume
@ stub FltDeviceIoControlFile
@ stub FltDoCompletionProcessingWhenSafe
@ stub FltEnumerateFilterInformation
@ stub FltEnumerateFilters
@ stub FltEnumerateInstanceInformationByFilter
@ stub FltEnumerateInstanceInformationByVolume
@ stub FltEnumerateInstances
@ stub FltEnumerateVolumeInformation
@ stub FltEnumerateVolumes
@ stub FltFlushBuffers
@ stub FltFreeCallbackData
@ stub FltFreeDeferredIoWorkItem
@ stub FltFreeFileLock
@ stub FltFreeGenericWorkItem
@ stub FltFreePoolAlignedWithTag
@ stub FltFreeSecurityDescriptor
@ stub FltFsControlFile
@ stub FltGetBottomInstance
@ stub FltGetContexts
@ stub FltGetDestinationFileNameInformation
@ stub FltGetDeviceObject
@ stub FltGetDiskDeviceObject
@ stub FltGetFileContext
@ stub FltGetFileNameInformation
@ stub FltGetFileNameInformationUnsafe
@ stub FltGetFilterFromInstance
@ stub FltGetFilterFromName
@ stub FltGetFilterInformation
@ stub FltGetInstanceContext
@ stub FltGetInstanceInformation
@ stub FltGetIrpName
@ stub FltGetLowerInstance
@ stub FltGetRequestorProcess
@ stub FltGetRequestorProcessId
@ stdcall FltGetRoutineAddress(str)
@ stub FltGetStreamContext
@ stub FltGetStreamHandleContext
@ stub FltGetSwappedBufferMdlAddress
@ stub FltGetTopInstance
@ stub FltGetTunneledName
@ stub FltGetUpperInstance
@ stub FltGetVolumeContext
@ stub FltGetVolumeFromDeviceObject
@ stub FltGetVolumeFromFileObject
@ stub FltGetVolumeFromInstance
@ stub FltGetVolumeFromName
@ stub FltGetVolumeGuidName
@ stub FltGetVolumeInstanceFromName
@ stub FltGetVolumeName
@ stub FltGetVolumeProperties
@ stub FltInitializeFileLock
@ stub FltInitializeOplock
@ stdcall FltInitializePushLock(ptr)
@ stub FltIs32bitProcess
@ stub FltIsCallbackDataDirty
@ stub FltIsDirectory
@ stub FltIsIoCanceled
@ stub FltIsOperationSynchronous
@ stub FltIsVolumeWritable
@ stub FltLoadFilter
@ stub FltLockUserBuffer
@ stub FltNotifyFilterChangeDirectory
@ stub FltObjectDereference
@ stub FltObjectReference
@ stub FltOpenVolume
@ stub FltOplockFsctrl
@ stub FltOplockIsFastIoPossible
@ stub FltParseFileName
@ stub FltParseFileNameInformation
@ stub FltPerformAsynchronousIo
@ stub FltPerformSynchronousIo
@ stub FltProcessFileLock
@ stub FltPurgeFileNameInformationCache
@ stub FltQueryEaFile
@ stub FltQueryInformationFile
@ stub FltQuerySecurityObject
@ stub FltQueryVolumeInformation
@ stub FltQueryVolumeInformationFile
@ stub FltQueueDeferredIoWorkItem
@ stub FltQueueGenericWorkItem
@ stub FltReadFile
@ stub FltReferenceContext
@ stub FltReferenceFileNameInformation
@ stdcall FltRegisterFilter(ptr ptr ptr)
@ stub FltReissueSynchronousIo
@ stub FltReleaseContext
@ stub FltReleaseContexts
@ stub FltReleaseFileNameInformation
@ stdcall FltReleasePushLock(ptr)
@ stub FltReleaseResource
@ stub FltRequestOperationStatusCallback
@ stub FltRetainSwappedBufferMdlAddress
@ stub FltReuseCallbackData
@ stub FltSendMessage
@ stub FltSetCallbackDataDirty
@ stub FltSetCancelCompletion
@ stub FltSetEaFile
@ stub FltSetFileContext
@ stub FltSetInformationFile
@ stub FltSetInstanceContext
@ stub FltSetSecurityObject
@ stub FltSetStreamContext
@ stub FltSetStreamHandleContext
@ stub FltSetVolumeContext
@ stub FltSetVolumeInformation
@ stdcall FltStartFiltering(ptr)
@ stub FltSupportsFileContexts
@ stub FltSupportsStreamContexts
@ stub FltSupportsStreamHandleContexts
@ stub FltTagFile
@ stub FltUninitializeFileLock
@ stub FltUninitializeOplock
@ stub FltUnloadFilter
@ stdcall FltUnregisterFilter(ptr)
@ stub FltUntagFile
@ stub FltWriteFile
