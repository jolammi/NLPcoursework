training_personID = exercise_data['training_personID']
testing_personID = exercise_data['testing_personID']

#Joining training/testing data matrices is done only for mfcc data. 

combined_personID = np.concatenate((training_personID, testing_personID))
combined_mfcc = np.concatenate((training_data_mfcc, testing_data_mfcc))
combined_class = np.concatenate((training_class, testing_class))


person_order = np.unique(combined_personID)
train_data_list = np.zeros((len(person_order), len(combined_personID)-10, 12))
test_data_list = np.zeros((len(person_order), len(combined_personID)-90, 12))
train_class_list = np.zeros((len(person_order), len(combined_personID)-10), dtype=int)
test_class_list = np.zeros((len(person_order), len(combined_personID)-90), dtype=int)

for i in range(len(person_order)):
    delete_rows = np.linspace(i*10, i*10+9, 10).astype(int)
    train_data_list[i,:] = np.delete(combined_mfcc, delete_rows, 0)
    test_data_list[i,:] = combined_mfcc[delete_rows]
    train_class_list[i,:] = np.delete(combined_class, delete_rows, 0)
    test_class_list[i,:] = combined_class[delete_rows]

svms = list()
for i in range(len(person_order)):
    svm_training_data = svm.SVC(kernel='poly', degree=3)
    svm_training_data.fit(train_data_list[i], train_class_list[i])
    svms.append(svm_training_data)
    
svm_test = np.zeros((len(person_order), 10), dtype=int)
svm_acc = np.zeros(10)

for i in range(len(person_order)):
    svm_test[i] = svms[i].predict(test_data_list[i])
    svm_acc[i] = accuracy_score(test_class_list[i], svm_test[i])

mean_svm_acc = np.mean(svm_acc)
sd_sv_acc = np.std(svm_acc)

print("Accuracy: ", svm_acc)
print("Accuracy mean: ", mean_svm_acc)
print("Accuracy SD: ", sd_sv_acc)