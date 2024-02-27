from network.model_architechure_bert_multi_scale import DocumentBertScoringModel
import torch

model = DocumentBertScoringModel()
torch.save(model.state_dict(),'models/model_bert.pth')
