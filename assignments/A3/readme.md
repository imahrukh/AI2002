# Neural Networks Report  
---

## 📖 Overview  
This report explores architectures, subtypes, applications, and supervised learning implementations of **Artificial Neural Networks (ANN)**, **Convolutional Neural Networks (CNN)**, and **Recurrent Neural Networks (RNN)**. It includes four practical applications with datasets, training details, and results.

---

## 🧠 Neural Network Architectures  
### **1. Artificial Neural Network (ANN)**  
- **Layers**: Input (structured data), hidden (dense layers), output (Sigmoid/Softmax/Linear).  
- **Activation**: ReLU, Softmax.  
- **Training**: Backpropagation with cross-entropy/MSE loss.  

### **2. Convolutional Neural Network (CNN)**  
- **Layers**: Convolutional (3x3 filters), pooling (max-pooling), flatten.  
- **Training**: Adam optimizer, sparse categorical cross-entropy.  

### **3. Recurrent Neural Network (RNN)**  
- **Cells**: LSTM/GRU for sequential data.  
- **Training**: BPTT with cross-entropy loss.  

---

## 🛠 Subtypes  
| **Network** | **Subtypes**       | **Key Features**                          |  
|-------------|--------------------|-------------------------------------------|  
| ANN         | MLP, GAN, Autoencoder | Classification, generation, compression  |  
| CNN         | ResNet, VGG        | Skip connections, deep layers            |  
| RNN         | LSTM, GRU, Bi-RNN  | Long-term dependencies, bidirectional    |  

---

## 🚀 Applications  
### **1. Image Classification (CIFAR-10)**  
- **Problem**: Classify 32x32 RGB images into 10 classes.  
- **Model**: CNN (Conv2D → MaxPooling → Flatten → Dense).  
- **Accuracy**: 85.6% on test set.  
- **Reference**: Krizhevsky et al. (2009).  

### **2. Stock Price Prediction (LSTM)**  
- **Problem**: Predict NASDAQ closing prices.  
- **Model**: LSTM (50 units) → Dropout → Dense.  
- **RMSE**: 1.8%.  
- **Reference**: Hochreiter & Schmidhuber (1997).  

### **3. Course Recommendation System**  
- **Problem**: Recommend courses using student interaction data.  
- **Model**: Neural Collaborative Filtering (NCF).  
- **NDCG@10**: 0.78.  
- **Reference**: He et al. (2017).  

### **4. Speech-to-Text (STT)**  
- **Problem**: Transcribe lectures using Whisper Transformer.  
- **WER**: 9.8%.  
- **Reference**: Radford et al. (2022).  

---

## 📚 Research Papers  
### **Image Classification**  
1. He et al., *Deep Residual Learning for Image Recognition* (IEEE CVPR 2016).  
2. Krizhevsky et al., *Learning Multiple Layers of Features from Tiny Images* (2009).  

### **Speech-to-Text**  
1. Radford et al., *Robust Speech Recognition via Large-Scale Weak Supervision* (2022).  
2. Zhao et al., *LoRS-Merging* (Springer 2025).  

### **Course Recommendation**  
1. He et al., *Neural Collaborative Filtering* (Springer WWW 2017).  

### **Stock Prediction**  
1. Hochreiter & Schmidhuber, *Long Short-Term Memory* (1997).  

---

## 📊 Results  
| **Application**               | **Metric**      | **Value** |  
|--------------------------------|-----------------|-----------|  
| Image Classification (CIFAR-10)| Test Accuracy   | 85.6%     |  
| Stock Prediction (LSTM)        | RMSE            | 1.8%      |  
| Course Recommendation (NCF)    | NDCG@10         | 0.78      |  
| Speech-to-Text (Whisper)       | WER             | 9.8%      |  

---

