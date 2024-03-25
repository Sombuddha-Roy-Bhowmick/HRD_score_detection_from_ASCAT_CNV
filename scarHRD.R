library("scarHRD")
score <- scar_score("scarHRD_Input.txt",reference = "grch38", chr.in.names=FALSE, seqz=FALSE)
write.table(score, "HRD_Score.txt",sep = "\t", quote = F, row.names = F)


