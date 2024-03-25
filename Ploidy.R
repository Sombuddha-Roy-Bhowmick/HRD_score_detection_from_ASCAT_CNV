getwd()
load(file = "ASCAT_objects.Rdata")
Ploidy <- ascat.output$ploidy
write.table(Ploidy, "Ploidy.txt",sep = "\t", quote = F, row.names = F)
