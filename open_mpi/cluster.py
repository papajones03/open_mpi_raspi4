from mpi4py import MPI
from ScapyUtil import ScapyUtil
from main import FileList

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
bcast_lst = []
file_lst = None

if rank == 0:
   file_lst = FileList().list_of_file()
   for i in range(0, size):
       bcast_lst.append(file_lst[i])
       file_lst.remove(file_lst[i])
    
else:
   bcast_lst = None
   
print(bcast_lst)
bcast_lst = comm.scatter(bcast_lst, root=0)
print(" File List in rank "+str(rank)+" File_Lst : "+bcast_lst)