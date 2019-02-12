import csv
import json

with open('cia.json') as json_data:
    cia_data = json.load(json_data)

    writeToCsv = csv.writer(open("cia_explanation.txt", "w+"))

    # writeToCsv.writerow([ 'Explanation_A', 'Explanation_B', 'Explanation_C', 'Explanation_D'])

    for cia_data in cia_data:
        writeToCsv.writerow([
            """&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160;&#160; The correct answer is """+ cia_data["correctAnswer"]+
            """<table class="question-container-table"><tbody><tr><td class=""><table width="100%" cellspacing="1" border="0"><tbody><tr><td class="">&nbsp;</td><td align="left" id="fact-pattern" class=""></td></tr><tr><td class="">&nbsp;</td><td class="center" id="question-images"></td></tr><tr><td align="left" width="105" valign="top" class=""></td><td align="left" id="highlightable" class=""><span id="queStem" class="">Explanation:</span></td></tr><tr id="foil-container"><td class=""></td><td align="left"><table><tbody><tr class="questionSpacing"><td class="questionLabelsCol"><label class="questionLetterLabel actualFoil actualActualFoil" for="answer-a">A.</label></td><td class=""><label class="actualFoil" for="answer-a">""" + cia_data["foils"][0]["explanation"] +
                            """</label></td></tr><tr class="questionSpacing"><td class="questionLabelsCol"><label class="questionLetterLabel actualFoil actualActualFoil" for="answer-b">B.</label></td><td class=""><label class="actualFoil" for="answer-b">""" + cia_data["foils"][1]["explanation"] +
                            """</label></td></tr><tr class="questionSpacing"><td class="questionLabelsCol"><label class="questionLetterLabel actualFoil actualActualFoil" for="answer-c">C.</label></td><td class=""><label class="actualFoil" for="answer-c">""" + cia_data["foils"][2]["explanation"] +
                            """</label></td></tr><tr class="questionSpacing"><td class="questionLabelsCol"><label class="questionLetterLabel actualFoil actualActualFoil" for="answer-d">D.</label></td><td class=""><label class="actualFoil" for="answer-d">""" + cia_data["foils"][3]["explanation"] +
                            """</label></td></tr></tbody></table></td></tr></tbody></table><br></td></tr></tbody></table><hr>"""
        ])