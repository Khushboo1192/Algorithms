#main function
# n is the number of vertices
# weights is a list of their weights, v_1, ..., v_n
def mwis (n, weights):
    #
    #FILL IN CODE HERE
    #
    opt=[];
    sol_tot_weight=0;
    sol_items=[];
    set_prev=[];
    set_curr=[];
    set_temp=[];

    opt.append(weights[0]);

    set_prev.append(1);

    if opt.__getitem__(0) > weights[1] :
        opt.append(weights[0]);
        set_curr.append(1);
        set_curr.append(0);
    else :
        opt.append(weights[1]);
        set_curr.append(0);
        set_curr.append(1);

    temp=0;
    count=0;

    for i in range(2,n):
        temp=opt[i-2]+weights[i];
        size=len(sol_items);
        print 'check if error ',temp,opt.__getitem__(i-1);
        if opt.__getitem__(i-1) > temp :
            opt.append(opt.__getitem__(i-1));
            set_prev=set_curr[:];
            set_curr.append(0);
        else :
            opt.append(temp);
            print'$$$$$$$$$$$$$$$$$'
            print 'printing prev array',set_prev;
            print 'printing curr array',set_curr;

            set_temp=set_curr[:];
            set_curr=set_prev[:];
            print 'printing curr array1',set_curr;
            print 'printing temp array1',set_temp;
            set_curr.append(0);
            set_curr.append(1);
            print 'printing curr array2',set_curr;
            set_prev=set_temp[:];
            del set_temp;
            print 'printing prev array3',set_prev;
            print 'printing curr array3',set_curr;
        print 'printing opt array '
        print ' '.join(map(str, opt));
        print 'printing prev array';
        print ' '.join(map(str,set_prev)) ;
        print 'printing curr array';
        print ' '.join(map(str,set_curr)) ; print '###############################################'

    for j in range(0,n):
        temp2=set_curr[j];
        print temp2;
        if(temp2>0) :
           sol_items.append(j);
    sol_tot_weight=opt[n-1];
    return (opt, sol_tot_weight, sorted(sol_items))


#YOU DO NOT NEED TO CHANGE THE CODE BELOW THIS LINE

#Read input
f = open("input.txt", "r")
weights = [int(x) for x in f.readline().split()]
n = len (weights)

#call mwis
(opt, sol_tot_weight, sol_items) = mwis(n, weights)

#output solution
print ' '.join(map(str, opt))
print sol_tot_weight
print ' '.join(map(str, sol_items))
