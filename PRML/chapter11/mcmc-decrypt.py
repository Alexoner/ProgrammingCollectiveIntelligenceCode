"""
Problem description:
This problem has got somewhat of a great pedigree as this method was suggested by Persi Diaconis- The Mathemagician. So Someone comes to you with the below text. This text looks like gibberish but this is a code, how to decrypyt it?

XZ STAVRK HXVR MYAZ OAKZM JKSSO SO MYR OKRR XDP JKSJRK XBMASD SO YAZ TWDHZ MYR JXMBYNSKF BSVRKTRM NYABY NXZ BXKRTRZZTQ OTWDH SVRK MYR AKSD ERPZMRXP KWZMTRP MYR JXTR OXBR SO X QSWDH NSIXD NXZ KXAZRP ORRETQ OKSI MYR JATTSN XDP X OXADM VSABR AIJRKORBMTQ XKMABWTXMRP MYR NSKPZ TRM IR ZRR MYR BYATP XDP PAR MYR ZWKHRSD YXP ERRD ZAMMADH NAMY YAZ OXBR MWKDRP MSNXKPZ MYR OAKR HAVADH MYR JXTIZ SO YAZ YXDPZ X NXKI XDP X KWE XTMRKDXMRTQ XZ MYR QSWDH NSIXD ZJSFR YR KSZR XDP XPVXDBADH MS MYR ERP Z YRXP ZXAP NAMY ISKR FADPDRZZ MYXD IAHYM YXVR ERRD RGJRBMRP SO YAI

Markov Chain Monte Carlo procesure:
1. Start by picking up a random current state.
2. Create a proposal for a new state by swapping two random letters in the current state.
3. Use a Scoring Function which calculates the score of the current state ScoreC and the proposed State ScoreP.
4. If the score of the proposed state is more than current state, Move to Proposed State.
5. Else flip a coin which has a probability of Heads ScoreP/ScoreC. If it comes heads move to proposed State.
6. Repeat from 2nd State.
"""
# AIM: To Decrypt a text using MCMC approach. i.e. find decryption key which we will call cipher from now on.
import string
import math
import random

# This function takes as input a decryption key and creates a dict for key where each letter in the decryption key
# maps to a alphabet For example if the decryption key is "DGHJKL...." this function will create a dict like {D:A,G:B,H:C....}
def create_cipher_dict(cipher):
    cipher_dict   = {}
    alphabet_list = list(string.ascii_uppercase)
    for i in range(len(cipher)):
        cipher_dict[alphabet_list[i]] = cipher[i]
    return cipher_dict

# This function takes a text and applies the cipher/key on the text and returns text.
def apply_cipher_on_text(text,cipher):
    cipher_dict = create_cipher_dict(cipher)
    text        = list(text)
    newtext     = ""
    for elem in text:
        if elem.upper() in cipher_dict:
            newtext+=cipher_dict[elem.upper()]
        else:
            newtext+=" "
    return newtext

# This function takes as input a path to a long text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
def create_scoring_params_dict(longtext_path):
    scoring_params = {}
    alphabet_list  = list(string.ascii_uppercase)
    with open(longtext_path) as fp:
        # text = fp.read().strip()
        # scoring_params = score_params_on_cipher(text)
        for line in fp:
            data = list(line.strip())
            for i in range(len(data)-1):
                alpha_i = data[i].upper()
                alpha_j = data[i+1].upper()
                if alpha_i not in alphabet_list and alpha_i != " ":
                    alpha_i = " "
                if alpha_j not in alphabet_list and alpha_j != " ":
                    alpha_j = " "
                key = alpha_i+alpha_j
                if key in scoring_params:
                    scoring_params[key]+=1
                else:
                    scoring_params[key]=1
    return scoring_params

# This function takes as input a text and creates scoring_params dict which contains the
# number of time each pair of alphabet appears together
# Ex. {'AB':234,'TH':2343,'CD':23 ..}
def score_params_on_cipher(text):
    scoring_params = {}
    alphabet_list  = list(string.ascii_uppercase)
    data           = list(text.strip())
    for i in range(len(data)-1):
        alpha_i = data[i].upper()
        alpha_j = data[i+1].upper()
        if alpha_i not in alphabet_list and alpha_i != " ":
            alpha_i = " "
        if alpha_j not in alphabet_list and alpha_j != " ":
            alpha_j = " "
        key = alpha_i+alpha_j
        if key in scoring_params:
            scoring_params[key]+=1
        else:
            scoring_params[key]=1
    return scoring_params

def get_cipher_score(text,cipher,scoring_params):
    """
     This function takes the text to be decrypted and a cipher to score the cipher.
     This function returns the log(score) metric
    """
    decrypted_text = apply_cipher_on_text(text,cipher)
    scored_f       = score_params_on_cipher(decrypted_text)
    cipher_score   = 0
    for k,v in scored_f.iteritems():
        if k in scoring_params:
            cipher_score += v*math.log(scoring_params[k])
    return cipher_score

# Generate a proposal cipher by swapping letters at two random location
def generate_cipher(cipher):
    pos1 = random.randint(0, len(list(cipher))-1)
    pos2 = random.randint(0, len(list(cipher))-1)
    if pos1 == pos2:
        return generate_cipher(cipher)
    else:
        cipher       = list(cipher)
        pos1_alpha   = cipher[pos1]
        pos2_alpha   = cipher[pos2]
        cipher[pos1] = pos2_alpha
        cipher[pos2] = pos1_alpha
        return "".join(cipher)

# Toss a random coin with robability of head p. If coin comes head return true else false.
def random_coin(p):
    unif = random.uniform(0,1)
    if unif>=p:
        return False
    else:
        return True

# Takes as input a text to decrypt and runs a MCMC algorithm for n_iter. Returns the state having maximum score and also
# the last few states
def MCMC_decrypt(n_iter,cipher_text,scoring_params):
    current_cipher = string.ascii_uppercase # Generate a random cipher to start
    state_keeper   = set()
    best_state     = ''
    score          = 0
    for i in range(n_iter):
        state_keeper.add(current_cipher)
        proposed_cipher        = generate_cipher(current_cipher)
        score_current_cipher   = get_cipher_score(cipher_text,current_cipher,scoring_params)
        score_proposed_cipher  = get_cipher_score(cipher_text,proposed_cipher,scoring_params)
        acceptance_probability = min(1,math.exp(score_proposed_cipher-score_current_cipher))
        if score_current_cipher>score:
            best_state = current_cipher
        if random_coin(acceptance_probability):
            # so it won't be stuck at local maxima
            current_cipher = proposed_cipher
        if i%500==0:
            print "iter",i,":",apply_cipher_on_text(cipher_text,current_cipher)[0:99]
    return state_keeper,best_state

## Run the Main Program:

scoring_params = create_scoring_params_dict('war_and_peace.txt')

plain_text = "As Oliver gave this first proof of the free and proper action of his lungs, \
the patchwork coverlet which was carelessly flung over the iron bedstead, rustled; \
the pale face of a young woman was raised feebly from the pillow; and a faint voice imperfectly \
articulated the words, Let me see the child, and die. \
The surgeon had been sitting with his face turned towards the fire: giving the palms of his hands a warm \
and a rub alternately. As the young woman spoke, he rose, and advancing to the bed's head, said, with more kindness \
than might have been expected of him: "

encryption_key = "XEBPROHYAUFTIDSJLKZMWVNGQC"
cipher_text    = apply_cipher_on_text(plain_text,encryption_key)
decryption_key = "ICZNBKXGMPRQTWFDYEOLJVUAHS"

print"Text To Decode:", cipher_text
print "\n"
states,best_state = MCMC_decrypt(10000,cipher_text,scoring_params)
print "\n"
print "Decoded Text:",apply_cipher_on_text(cipher_text,best_state)
print "\n"
print "MCMC KEY FOUND:",best_state
print "ACTUAL DECRYPTION KEY:",decryption_key
