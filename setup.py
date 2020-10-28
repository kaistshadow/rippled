from distutils.command.build_ext import build_ext
from distutils.core import setup, Extension
import os
import shutil

def exec_shell_cmd(cmd):
    if os.system(cmd) != 0:
        print("error while executing '%s'" % cmd)
        exit(-1)

def create_ripple():
    exec_shell_cmd("rm -rf build")
    exec_shell_cmd("mkdir build && cd build && cmake .. && make -j 8")


def create_libarchive():
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/libarchive && rm -rf build2")
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/libarchive && mkdir build2 && cd build2 && cmake .. && make -j 4")


def create_soci():
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci && rm -rf build")
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci && mkdir build && cd build && cmake .. && make -j 4")

def create_sqlite3():
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/sqlite3 && rm -rf build")
    exec_shell_cmd("cd .nih_c/unix_makefiles/GNU_7.5.0/Release/src/sqlite3 && mkdir build && cd build && cmake .. && make -j 4")

        

if __name__ == '__main__':

    path_libarchive = './.nih_c/unix_makefiles/GNU_7.5.0/Release/src/libarchive/build2/libarchive'
    path_sqlite3 = './.nih_c/unix_makefiles/GNU_7.5.0/Release/src/sqlite3/build'
    path_soci = './.nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci/build/lib'
    path_protobuf = './../../protobuf/protobuf/src/.libs'
    path_boost = './../../boost/boost_1_70_0/stage/lib'

    path_libarchive = os.path.abspath(path_libarchive)
    path_sqlite3 = os.path.abspath(path_sqlite3)
    path_soci = os.path.abspath(path_soci)
    path_protobuf = os.path.abspath(path_protobuf)
    path_boost = os.path.abspath(path_boost)
    target = "cd build && /usr/bin/c++ -fPIC  -Wall -Wdeprecated -Wextra -Wno-unused-parameter -O3 -DNDEBUG -rdynamic -Wl,--no-as-needed -shared -Wl,-soname,librippled.so -o librippled.so CMakeFiles/rippled.dir/src/ripple/app/consensus/RCLConsensus.cpp.o CMakeFiles/rippled.dir/src/ripple/app/consensus/RCLCxPeerPos.cpp.o CMakeFiles/rippled.dir/src/ripple/app/consensus/RCLValidations.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/AcceptedLedger.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/AcceptedLedgerTx.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/AccountStateSF.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/BookListeners.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/ConsensusTransSetSF.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/Ledger.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/LedgerHistory.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/OrderBookDB.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/TransactionStateSF.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/BuildLedger.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/InboundLedger.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/InboundLedgers.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/InboundTransactions.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/LedgerCleaner.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/LedgerMaster.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/LedgerReplay.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/LedgerToJson.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/LocalTxs.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/OpenLedger.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/TransactionAcquire.cpp.o CMakeFiles/rippled.dir/src/ripple/app/ledger/impl/TransactionMaster.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/Application.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/BasicApp.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/CollectorManager.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/GRPCServer.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/LoadManager.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/Main.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/NodeIdentity.cpp.o CMakeFiles/rippled.dir/src/ripple/app/main/NodeStoreScheduler.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/CanonicalTXSet.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/FeeVoteImpl.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/HashRouter.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/NegativeUNLVote.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/NetworkOPs.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/SHAMapStoreImp.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/detail/impl/WorkSSL.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/AccountTxPaging.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/AmendmentTable.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/LoadFeeTrack.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/Manifest.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/Transaction.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/TxQ.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/ValidatorKeys.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/ValidatorList.cpp.o CMakeFiles/rippled.dir/src/ripple/app/misc/impl/ValidatorSite.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/AccountCurrencies.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/Credit.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/Flow.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/PathRequest.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/PathRequests.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/Pathfinder.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/RippleCalc.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/RippleLineCache.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/RippleState.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/impl/BookStep.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/impl/DirectStep.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/impl/PaySteps.cpp.o CMakeFiles/rippled.dir/src/ripple/app/paths/impl/XRPEndpointStep.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/ApplyContext.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/BookTip.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/CancelCheck.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/CancelOffer.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/CashCheck.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/Change.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/CreateCheck.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/CreateOffer.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/CreateTicket.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/DeleteAccount.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/DepositPreauth.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/Escrow.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/InvariantCheck.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/OfferStream.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/PayChan.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/Payment.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/SetAccount.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/SetRegularKey.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/SetSignerList.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/SetTrust.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/SignerEntries.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/Taker.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/Transactor.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/apply.cpp.o CMakeFiles/rippled.dir/src/ripple/app/tx/impl/applySteps.cpp.o CMakeFiles/rippled.dir/src/ripple/basics/impl/Archive.cpp.o CMakeFiles/rippled.dir/src/ripple/basics/impl/BasicConfig.cpp.o CMakeFiles/rippled.dir/src/ripple/basics/impl/PerfLogImp.cpp.o CMakeFiles/rippled.dir/src/ripple/basics/impl/ResolverAsio.cpp.o CMakeFiles/rippled.dir/src/ripple/basics/impl/UptimeClock.cpp.o CMakeFiles/rippled.dir/src/ripple/basics/impl/make_SSLContext.cpp.o CMakeFiles/rippled.dir/src/ripple/basics/impl/mulDiv.cpp.o CMakeFiles/rippled.dir/src/ripple/conditions/impl/Condition.cpp.o CMakeFiles/rippled.dir/src/ripple/conditions/impl/Fulfillment.cpp.o CMakeFiles/rippled.dir/src/ripple/conditions/impl/error.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/Config.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/DatabaseCon.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/Job.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/JobQueue.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/LoadEvent.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/LoadMonitor.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/SNTPClock.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/SociDB.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/Stoppable.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/TimeKeeper.cpp.o CMakeFiles/rippled.dir/src/ripple/core/impl/Workers.cpp.o CMakeFiles/rippled.dir/src/ripple/consensus/Consensus.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/ApplyStateTable.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/ApplyView.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/ApplyViewBase.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/ApplyViewImpl.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/BookDirs.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/CachedSLEs.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/CachedView.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/CashDiff.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/Directory.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/OpenView.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/PaymentSandbox.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/RawStateTable.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/ReadView.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/TxMeta.cpp.o CMakeFiles/rippled.dir/src/ripple/ledger/impl/View.cpp.o CMakeFiles/rippled.dir/src/ripple/net/impl/DatabaseDownloader.cpp.o CMakeFiles/rippled.dir/src/ripple/net/impl/HTTPClient.cpp.o CMakeFiles/rippled.dir/src/ripple/net/impl/InfoSub.cpp.o CMakeFiles/rippled.dir/src/ripple/net/impl/RPCCall.cpp.o CMakeFiles/rippled.dir/src/ripple/net/impl/RPCErr.cpp.o CMakeFiles/rippled.dir/src/ripple/net/impl/RPCSub.cpp.o CMakeFiles/rippled.dir/src/ripple/net/impl/RegisterSSLCerts.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/backend/MemoryFactory.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/backend/NuDBFactory.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/backend/NullFactory.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/backend/RocksDBFactory.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/BatchWriter.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/Database.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/DatabaseNodeImp.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/DatabaseRotatingImp.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/DatabaseShardImp.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/DecodedBlob.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/DummyScheduler.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/EncodedBlob.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/ManagerImp.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/NodeObject.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/Shard.cpp.o CMakeFiles/rippled.dir/src/ripple/nodestore/impl/TaskQueue.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/Cluster.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/ConnectAttempt.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/Handshake.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/Message.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/OverlayImpl.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/PeerImp.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/PeerReservationTable.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/PeerSet.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/ProtocolVersion.cpp.o CMakeFiles/rippled.dir/src/ripple/overlay/impl/TrafficCount.cpp.o CMakeFiles/rippled.dir/src/ripple/peerfinder/impl/Bootcache.cpp.o CMakeFiles/rippled.dir/src/ripple/peerfinder/impl/Endpoint.cpp.o CMakeFiles/rippled.dir/src/ripple/peerfinder/impl/PeerfinderConfig.cpp.o CMakeFiles/rippled.dir/src/ripple/peerfinder/impl/PeerfinderManager.cpp.o CMakeFiles/rippled.dir/src/ripple/peerfinder/impl/SlotImp.cpp.o CMakeFiles/rippled.dir/src/ripple/peerfinder/impl/SourceStrings.cpp.o CMakeFiles/rippled.dir/src/ripple/resource/impl/Charge.cpp.o CMakeFiles/rippled.dir/src/ripple/resource/impl/Consumer.cpp.o CMakeFiles/rippled.dir/src/ripple/resource/impl/Fees.cpp.o CMakeFiles/rippled.dir/src/ripple/resource/impl/ResourceManager.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountChannels.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountCurrenciesHandler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountInfo.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountLines.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountObjects.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountOffers.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountTx.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountTxOld.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/AccountTxSwitch.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/BlackList.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/BookOffers.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/CanDelete.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Connect.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/ConsensusInfo.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/CrawlShards.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/DepositAuthorized.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/DownloadShard.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Feature1.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Fee1.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/FetchInfo.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/GatewayBalances.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/GetCounts.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerAccept.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerCleanerHandler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerClosed.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerCurrent.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerData.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerEntry.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerHandler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerHeader.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LedgerRequest.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LogLevel.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/LogRotate.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Manifest.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/NoRippleCheck.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/OwnerInfo.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/PathFind.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/PayChanClaim.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Peers.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Ping.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Print.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Random.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Reservations.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/RipplePathFind.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/ServerInfo.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/ServerState.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/SignFor.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/SignHandler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Stop.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Submit.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/SubmitMultiSigned.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Subscribe.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/TransactionEntry.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Tx.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/TxHistory.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/UnlList.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Unsubscribe.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/ValidationCreate.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/ValidatorInfo.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/ValidatorListSites.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/Validators.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/handlers/WalletPropose.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/DeliveredAmount.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/Handler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/GRPCHelpers.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/LegacyPathFind.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/RPCHandler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/RPCHelpers.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/Role.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/ServerHandlerImp.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/ShardArchiveHandler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/ShardVerificationScheduler.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/Status.cpp.o CMakeFiles/rippled.dir/src/ripple/rpc/impl/TransactionSign.cpp.o CMakeFiles/rippled.dir/src/ripple/server/impl/JSONRPCUtil.cpp.o CMakeFiles/rippled.dir/src/ripple/server/impl/Port.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/NodeFamily.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/SHAMap.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/SHAMapDelta.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/SHAMapItem.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/SHAMapNodeID.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/SHAMapSync.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/SHAMapTreeNode.cpp.o CMakeFiles/rippled.dir/src/ripple/shamap/impl/ShardFamily.cpp.o libxrpl_core.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/libarchive/build2/libarchive/libarchive.so ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/sqlite3/build/libsqlite3.so ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci-build/lib/libsoci_empty.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci/build/lib/libsoci_sqlite3.so ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/soci/build/lib/libsoci_core.so ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/rocksdb-build/librocksdb.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/lz4-build/liblz4.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/snappy-build/libsnappy.a libpbufs.a libgrpc_pbufs.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/grpc_src-build/libgrpc++_unsecure.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/grpc_src-build/libgrpc_unsecure.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/grpc_src-build/libgpr.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/grpc_src-build/libaddress_sorting.a ./../.nih_c/unix_makefiles/GNU_7.5.0/Release/src/c-ares_src-build/_installed_/lib/libcares.a ./../../../protobuf/protobuf/src/.libs/libprotobuf.so ./../../../boost/boost_1_70_0/stage/lib/libboost_coroutine.a ./../../../boost/boost_1_70_0/stage/lib/libboost_context.a ./../../../boost/boost_1_70_0/stage/lib/libboost_filesystem.so ./../../../boost/boost_1_70_0/stage/lib/libboost_program_options.so  ./../../../boost/boost_1_70_0/stage/lib/libboost_regex.so ./../../../boost/boost_1_70_0/stage/lib/libboost_system.a ./../../../boost/boost_1_70_0/stage/lib/libboost_thread.so ./../../../boost/boost_1_70_0/stage/lib/libboost_chrono.a ./../../../boost/boost_1_70_0/stage/lib/libboost_date_time.a ./../../../boost/boost_1_70_0/stage/lib/libboost_atomic.a -pthread -ldl -lrt libsecp256k1.a libed25519-donna.a -rdynamic -static-libstdc++ -fuse-ld=gold -Wl,-rpath," + path_libarchive + ":" + path_sqlite3 + ":" + path_soci + ":" + path_protobuf + ":" + path_boost + " -Wl,--no-as-needed /usr/lib/x86_64-linux-gnu/libssl.a /usr/lib/x86_64-linux-gnu/libcrypto.a /usr/lib/x86_64-linux-gnu/libz.so"

    # exec_shell_cmd("export BOOST_ROOT=~/boost_1_70_0")
    # # create_ripple()
    # create_libarchive()
    # create_sqlite3()
    # create_soci()
    exec_shell_cmd(target)
