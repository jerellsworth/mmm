#!/usr/bin/env python3

import mido

state = [None for _ in range(16)]
with mido.open_input('Midinous Port') as inport:
    with mido.open_output('mmm', virtual=True) as outport:
        for msg in inport:
            print(msg)
            outport.send(msg)
            if msg.type == 'note_off':
                state[msg.channel] = None
                for c, note in enumerate(state):
                    if note is not None:
                        off_msg = mido.Message(
                            'note_off',
                            channel=c,
                            note=state[c],
                            velocity=100,
                            time=0)
                        print(off_msg)
                        outport.send(off_msg)
                for c, note in enumerate(state):
                    if note is not None:
                        on_msg = mido.Message(
                            'note_on',
                            channel=c,
                            note=state[c],
                            velocity=100,
                            time=0)
                        print(on_msg)
                        outport.send(on_msg)
            elif msg.type == 'note_on':
                state[msg.channel] = msg.note
