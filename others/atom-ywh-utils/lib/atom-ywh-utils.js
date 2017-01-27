'use babel';

import atomYwhUtilsView from './atom-ywh-utils-view'
import atomYwhUtilsView2 from './atom-ywh-utils-view2'
import {
    CompositeDisposable
} from 'atom'

export default {

    atomYwhUtilsView: null,
    modalPanel: null,
    modalPanel2: null,
    subscriptions: null,

    activate(state) {

        this.atomYwhUtilsView = new atomYwhUtilsView(state.atomYwhUtilsViewState)
        this.modalPanel = atom.workspace.addModalPanel({
            item: this.atomYwhUtilsView.getElement(),
            visible: false
        })
        this.atomYwhUtilsView2 = new atomYwhUtilsView2(state.atomYwhUtilsViewState)
        this.modalPanel2 = atom.workspace.addModalPanel({
            item: this.atomYwhUtilsView2.getElement(),
            visible: false
        })

        // Events subscribed to in atom's system can be easily cleaned up with a CompositeDisposable
        this.subscriptions = new CompositeDisposable()

        // Register command that toggles this view

        this.subscriptions.add(atom.commands.add('atom-workspace', {
            'atom-ywh-utils:toggle': () => this.toggle(),
            'atom-ywh-utils:scrollUp10rows': () => this.scrollUp10rows(),
            'atom-ywh-utils:scrollDown10rows': () => this.scrollDown10rows(),
            'atom-ywh-utils:repeate by times': () => this.repeateByTimes(),
            'atom-ywh-utils:evalSelected': () => this.evalSelected(),
            'atom-ywh-utils:paste after': () => this.pasteAfter()
        }))

        // iframe=document.getElementById('ywh-web-view-frame');
        // iframe.contentWindow.document.body.backcolor="#000000";

    },

    deactivate() {
        this.modalPanel.destroy()
        this.subscriptions.dispose()
        this.atomYwhUtilsView.destroy()
    },

    serialize() {
        return {
            atomYwhUtilsViewState: this.atomYwhUtilsView.serialize()
        }
    },

    toggle() {
        if (this.modalPanel.isVisible) {
            editor = atom.workspace.getActiveTextEditor()
            searchText = editor.getSelectedText()
            iframe = document.getElementById('ywh-web-view-frame')
            if (searchText != null) {
                iframe.src = encodeURI("http://wap.baidu.com/s?word=" + searchText)
            }
        }

        return (
            this.modalPanel.isVisible() ?
            this.modalPanel.hide() :
            this.modalPanel.show()
        );
    },

    scrollUp10rows() {
        atom.workspace.getActiveTextEditor().moveUp(10)
    },

    scrollDown10rows() {
        atom.workspace.getActiveTextEditor().moveDown(10)
    },

    //Repeate Text By Times
    repeateByTimes() {
        editor = atom.workspace.getActiveTextEditor()
        textSelected = editor.getSelectedText()
        str = ''
        if (textSelected.indexOf('*') > 0) {
            val = textSelected.split('*')[0].toString()
            times = parseInt(textSelected.split('*')[1])
            for (i = 0; i < times; i++) {
                str += val
            }
        }
        editor.insertText(str);
    },
    evalSelected() {
        editor = atom.workspace.getActiveTextEditor()
        textSelected = editor.getSelectedText()
        str = eval(textSelected)
        editor.insertText(str)
    },
    // insert a string into other string's end 
    pasteAfter() {
        editor = atom.workspace.getActiveTextEditor()
        textSelected = editor.getSelectedText()
        clipboard1 = atom.clipboard.read()
        clipboards = clipboard1.split('\r\n')
        texts = textSelected.split('\r\n')
        returnstr = ''
        let i = 0
        clipboards.forEach((clip) => {
            returnstr += texts[i] + clip + '\r\n'
            i++
        })
        returnstr = returnstr.trimRight('\r\n')
        editor.insertText(returnstr)
    }

};