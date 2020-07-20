# OSC-ReRouter

OSC ReRouter is a very simple Python script that takes arguments from OSC messages and adds them on to the end of the address with a new prefix. It was created as a way of converting messages that FileMaker's MBS cannot read into ones that it can.


It is dependent on py-osc.


Run the script and it'll ask for:
RX IP Address
RX Port
TX IP Address
TX Port
The message to listen for (* is wildcard)
Then the new message prefix

It'll print out any message it transmits.


Example Input:
/eos/out/softkey/1, Make Man(s)


Example Output:
/reRouter/eos/out/softkey/1/Make Man, 0(s)

