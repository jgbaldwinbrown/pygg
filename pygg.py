#!/usr/bin/env python3

import subprocess
import pandas as pd
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return obj.to_json(orient='records')
        return json.JSONEncoder.default(self, obj)

class DictEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'to_dict'):
            return obj.to_dict(orient='list')
        return json.JSONEncoder.default(self, obj)

def ggplot(jdata, command):
    proc = subprocess.Popen(
        [
            "ggplotit",
            command
        ],
        stdin=subprocess.PIPE
    )
    #proc.communicate(input = data_frame.to_csv(sep="\t", index=None).encode('utf-8'))
    proc.communicate(input = json.dumps(jdata, cls=DictEncoder).encode('utf-8'))

def main():
    # quick test of ggplot
    # should only run if not loading as a library
    
    a = pd.DataFrame({"b": [1,2,3], "c": [4,5,6]})
    ggplot_data = {"data": a, "extra": 1}
    print(json.dumps(ggplot_data, cls=DictEncoder))
    command = """
    print(jdata$extra)
    print(data)
    pdf("test_out.pdf", height=3, width=4)
    print(ggplot(data=data, aes(b, c)) + geom_point())
    dev.off()
    """
    ggplot(ggplot_data, command)

if __name__ == "__main__":
    main()
