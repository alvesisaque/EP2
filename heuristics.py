import util


def h_naive(state, planning):
    return 0


def h_add(state, planning):
    '''
    Return heuristic h_add value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    h = dict() 
    actions = planning.actions
    #init = planning.problem.init
    X = state
    for x in X:
        h[x] = 0
    change = True
    while change:
        change = False
        actionsApplicable = applicable(X,actions)
        for a in actionsApplicable:
            X = successorRelaxed(X,a) #added positive effects of a
            for p in a.pos_effect:
                prev = h.get(p,sys.maxsize)
                h[p] = min(prev,(1+sum(h.get(pre, sys.maxsize) for pre in a.precond)))
                if prev != h[p]:
                    change = True
    return h


def h_max(state, planning):
    '''
    Return heuristic h_max value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '


def h_ff(state, planning):
    '''
    Return heuristic h_ff value for `state`.

    OBSERVATION: It receives `planning` object in order
    to access the applicable actions and problem information.
    '''
    util.raiseNotDefined()
    ' YOUR CODE HERE '
