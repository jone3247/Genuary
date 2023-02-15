# Fun Art Projects

Personal art projects! Some from the Genuary challenge, some just my own. Some complicated, some mysteriously simple. 

## Examples

**random-walk-graphs** : Based on the 2022 Genuary art prompt: Create your own pseudo-random number generator and visually check the results. This piece generates a random walk on a canvas and then connects all the adjacent points to create a nebulus rorschach-like image. What do you see?

<p align='center'>
  <img src="https://github.com/mwdjones/art-projects/blob/main/random-walk-graphs/Jan24_4.png" width=50% height=50%>
</p>

*Sample random walk code*

```python
for j in range(0, 5):
    n = 1000 #steps to take
    
    x = np.zeros(n)
    y = np.zeros(n)
    
    for i in range(1, n):
        m = rand.randint(0, 3)
        
        if(m == 0): #0 --> y is constant, x increases
            x[i] = x[i-1] + 1
            y[i] = y[i-1]
        if(m == 1): #1 --> y increases, x is constant
            x[i] = x[i-1] 
            y[i] = y[i-1] + 1
        if(m == 2): #2 --> y is constant, x decreases
            x[i] = x[i-1] - 1
            y[i] = y[i-1]
        if(m == 3): #3 --> y decreases, x is constant
            x[i] = x[i-1] 
            y[i] = y[i-1] - 1

```

**hitomezashi-stitches** : Develops an algorithm for randomly generating a pattern of Hitomezashi stitches ([check it out!](https://www.bing.com/ck/a?!&&p=31c0e8c6f0134d63JmltdHM9MTY3NTk4NzIwMCZpZ3VpZD0zM2VlZDg3NS1mODU4LTY5ODYtMmY5ZC1jYTA3Zjk4YjY4MTMmaW5zaWQ9NTIxOA&ptn=3&hsh=3&fclid=33eed875-f858-6986-2f9d-ca07f98b6813&psq=hitomezashi+stitch+patterns&u=a1aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g_dj1KYmZoemxNazJlWQ&ntb=1)) and then creates a short animation of the 'stitching'. 

<p align='center'>
  <img src="https://github.com/mwdjones/art-projects/blob/main/hitomezashi-stitches/figs/line.gif" width=50% height=50%>
</p>

