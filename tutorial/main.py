from pocketsphinx import LiveSpeech


hmm = '../Model/Model_SR_16000/model_parameters/dataset.cd_cont_200'
lm ='dataset/etc/dataset.lm.bin'
dict = 'dataset/etc/dataset.dict'

recognizer = LiveSpeech(verbose=False, sampling_rate=16000, buffer_size=2048, no_search=False, full_utt=False, hmm=hmm,lm=lm, dict=dict)

for phrase in recognizer:
    print(phrase)